"""Validate all questions and write docs/<exam>/index.html (self-contained, GitHub Pages ready),
plus docs/index.html that links to every built exam."""
import json
import os
import re
import sys

import exam  # python build.py <exam>; must come before objectives

from objectives import DOMAINS, EXAM, EXAM_TITLE, GROUPS, TOTAL, objectives
from validate import check, load, load_cases

partial = "--partial" in sys.argv  # preview with whatever groups exist so far
qs = load(list(GROUPS))
err = [] if partial else check(qs, list(GROUPS))
if not partial and (err or len(qs) != TOTAL):
    sys.exit(f"not building: {len(err)} validation errors, {len(qs)} questions (run validate.py)")

data = {
    "exam": {"id": EXAM, "title": EXAM_TITLE},
    "domains": {k: {"title": t, "weight": w} for k, (t, w) in DOMAINS.items()},
    "objectives": {k: t for k, (t, _) in objectives().items()},
    "questions": qs,
    "cases": {c["id"]: c for c in load_cases()},
}
# "</" would close the <script> tag early.
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
with open(os.path.join(exam.ROOT, "template.html"), encoding="utf-8") as f:
    html = f.read().replace("/*__DATA__*/", blob).replace("__EXAM_TITLE__", EXAM_TITLE).replace("__EXAM__", EXAM)
out = os.path.join(exam.ROOT, "docs", exam.KEY)
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print(f"docs/{exam.KEY}/index.html: {len(qs)} questions, {len(html) // 1024} KB")

# landing page: one link per exam that has been built
LEVELS = {1: "Entry / business", 2: "Associate", 3: "Expert"}
CATEGORY_ORDER = ["AI", "Data", "Microsoft 365", "GitHub"]  # other categories follow alphabetically
found = []  # (category, level, exam id, folder, title)
for k in exam.EXAMS:
    if os.path.isfile(os.path.join(exam.ROOT, "docs", k, "index.html")):
        with open(os.path.join(exam.ROOT, "exams", k, "objectives.py"), encoding="utf-8") as f:
            src = f.read()
        eid, title = (re.search(rf'^{v} = "(.*)"', src, re.M).group(1) for v in ("EXAM", "EXAM_TITLE"))
        # optional settings in objectives.py: CATEGORY = "AI", LEVEL = 1 (entry), 2 (associate), 3 (expert)
        cat = re.search(r'^CATEGORY = "(.*)"', src, re.M)
        lvl = re.search(r"^LEVEL = (\d)", src, re.M)
        found.append((cat.group(1) if cat else "Other", int(lvl.group(1)) if lvl else 2, eid, k, title))
found.sort(key=lambda x: (CATEGORY_ORDER.index(x[0]) if x[0] in CATEGORY_ORDER else len(CATEGORY_ORDER), x[0], x[1], x[2]))
links = []
for i, (cat, lvl, eid, k, title) in enumerate(found):
    if i == 0 or found[i - 1][0] != cat:
        links.append(f"{'</ul>' if i else ''}<h2>{cat}</h2><ul>")
    links.append(f'<li><a href="{k}/"><b>{eid}</b> {title}<span class="lvl">{LEVELS.get(lvl, "")}</span></a></li>')
if links:
    links.append("</ul>")
with open(os.path.join(exam.ROOT, "docs", "index.html"), "w", encoding="utf-8") as f:
    f.write(f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Exam Buddy</title>
<style>
:root {{ color-scheme: light dark; --bg: #f6f7f9; --card: #fff; --text: #1b1f24; --accent: #2563eb; --line: #d8dde3; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg: #111418; --card: #1a1e24; --text: #e6e9ee; --accent: #6ea8ff; --line: #2c323a; }} }}
body {{ margin: 0; background: var(--bg); color: var(--text); font: 16px/1.55 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }}
main {{ max-width: 860px; margin: 0 auto; padding: 24px 16px 64px; overflow-wrap: anywhere; }}
ul {{ list-style: none; padding: 0; }}
a {{ display: block; padding: 16px; margin: 0 0 12px; background: var(--card); border: 1px solid var(--line); border-radius: 12px; color: var(--text); text-decoration: none; }}
a:hover, a:focus-visible {{ border-color: var(--accent); }}
b {{ color: var(--accent); margin-right: 6px; }}
h2 {{ margin: 28px 0 12px; font-size: 1.15rem; }}
.lvl {{ float: right; margin-left: 12px; font-size: .8rem; opacity: .7; }}
</style></head>
<body><main><h1>Exam Buddy</h1><p>Practice exams for Microsoft certifications. Original questions, not real exam questions.</p>
{"".join(links)}</main></body></html>
""")

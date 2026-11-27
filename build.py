"""Validate all questions and write docs/<exam>/index.html (self-contained, GitHub Pages ready),
plus docs/index.html that links to every built exam."""
import json
import os
import re
import sys

import exam  # python build.py <exam>; must come before objectives

from objectives import DOMAINS, EXAM, EXAM_TITLE, GROUPS, TOTAL, objectives
from validate import check, load, load_cases

import datetime

import objectives as _settings  # optional page settings: CATEGORY, CONTENT_DATE

partial = "--partial" in sys.argv  # preview with whatever groups exist so far

# Per category: (light colour, dark colour, note). The colour marks the exam on the start page and
# in the exam page; the note is shown on both. Colours keep 4.5:1 contrast with white / dark text.
CATEGORY_STYLE = {
    "Anthropic": ("#c2410c", "#f59e6c",
                  "Unofficial practice questions. Anthropic's certification exams are built differently from the "
                  "Microsoft exams (their own scenario formats, and Anthropic does not publish a free study guide), "
                  "so these questions are less realistic than the Microsoft ones. Use them to learn the concepts, "
                  "not to predict the exam."),
}
STALE_MONTHS = 6  # the pages show "may be outdated" when CONTENT_DATE is older than this
_cat = getattr(_settings, "CATEGORY", None)
_style = CATEGORY_STYLE.get(_cat)
ACCENT_CSS = ""
if _style:
    ACCENT_CSS = (f':root {{ --accent: {_style[0]}; --accent-text: #ffffff; }}\n'
                  f'@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --accent: {_style[1]}; --accent-text: #0b0d10; }} }}\n'
                  f':root[data-theme="dark"] {{ --accent: {_style[1]}; --accent-text: #0b0d10; }}')
qs = load(list(GROUPS))
err = [] if partial else check(qs, list(GROUPS))
if not partial and (err or len(qs) != TOTAL):
    sys.exit(f"not building: {len(err)} validation errors, {len(qs)} questions (run validate.py)")

data = {
    "exam": {"id": EXAM, "title": EXAM_TITLE, "notice": _style[2] if _style else "",
             "contentDate": getattr(_settings, "CONTENT_DATE", "")},
    "domains": {k: {"title": t, "weight": w} for k, (t, w) in DOMAINS.items()},
    "objectives": {k: t for k, (t, _) in objectives().items()},
    "questions": qs,
    "cases": {c["id"]: c for c in load_cases()},
}
# "</" would close the <script> tag early.
blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
with open(os.path.join(exam.ROOT, "template.html"), encoding="utf-8") as f:
    html = (f.read().replace("/*__DATA__*/", blob).replace("/*__ACCENT__*/", ACCENT_CSS)
            .replace("__EXAM_TITLE__", EXAM_TITLE).replace("__EXAM__", EXAM))
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
        cdate = re.search(r'^CONTENT_DATE = "(\d{4}-\d{2})"', src, re.M)  # optional: month the content was last checked
        found.append((cat.group(1) if cat else "Other", int(lvl.group(1)) if lvl else 2, eid, k, title,
                      cdate.group(1) if cdate else ""))
found.sort(key=lambda x: (CATEGORY_ORDER.index(x[0]) if x[0] in CATEGORY_ORDER else len(CATEGORY_ORDER), x[0], x[1], x[2]))
today = datetime.date.today()
links = []
cat_css = []
for i, (cat, lvl, eid, k, title, cdate) in enumerate(found):
    style = CATEGORY_STYLE.get(cat)
    slug = re.sub(r"[^a-z0-9]+", "-", cat.lower())
    if i == 0 or found[i - 1][0] != cat:
        note = f'<p class="cnote">{style[2]}</p>' if style else ""
        links.append(f"{'</ul>' if i else ''}<h2>{cat}</h2>{note}<ul>")
        if style:
            cat_css.append(f".cat-{slug} {{ --c: {style[0]}; }}\n"
                           f"@media (prefers-color-scheme: dark) {{ .cat-{slug} {{ --c: {style[1]}; }} }}")
    stars = "&#9733;" * lvl if lvl in LEVELS else ""  # filled stars only, no empty ones
    when = ""
    if cdate:
        y, m = map(int, cdate.split("-"))
        when = f'<small class="when" data-date="{cdate}">Content as of {datetime.date(y, m, 1):%B %Y}</small>'
        if (today.year - y) * 12 + today.month - m > STALE_MONTHS:
            print(f"WARNING: {eid} content is from {cdate}, older than {STALE_MONTHS} months: re-check it and update CONTENT_DATE")
    links.append(f'<li><a class="cat-{slug}" href="{k}/"><b>{eid}</b> {title}<span class="lvl" role="img" '
                 f'aria-label="Level {lvl} of 3: {LEVELS.get(lvl, "")}" title="{LEVELS.get(lvl, "")}">{stars}</span>{when}</a></li>')
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
a {{ display: block; padding: 16px; margin: 0 0 12px; background: var(--card); border: 1px solid var(--line); border-left: 4px solid var(--c, var(--line)); border-radius: 12px; color: var(--text); text-decoration: none; }}
a:hover, a:focus-visible {{ border-color: var(--c, var(--accent)); }}
b {{ color: var(--c, var(--accent)); margin-right: 6px; }}
h2 {{ margin: 28px 0 12px; font-size: 1.15rem; }}
.lvl {{ float: right; margin-left: 12px; font-size: .8rem; opacity: .7; color: var(--c, var(--text)); }}
.cnote {{ margin: -4px 0 12px; font-size: .9rem; opacity: .85; }}
.when {{ display: block; margin-top: 4px; font-size: .8rem; opacity: .7; }}
.when.old {{ color: var(--c, var(--accent)); opacity: 1; }}
{chr(10).join(cat_css)}
</style></head>
<body><main><h1>Exam Buddy</h1><p>Practice exams for Microsoft certifications. Original questions, not real exam questions.</p>
{"".join(links)}</main>
<script>
// the label ages by itself: more than {STALE_MONTHS} months after the content date it says so
document.querySelectorAll(".when").forEach(function (el) {{
  var p = el.dataset.date.split("-"), months = (new Date().getFullYear() - +p[0]) * 12 + new Date().getMonth() + 1 - +p[1];
  if (months > {STALE_MONTHS}) {{ el.classList.add("old"); el.textContent += " - may be outdated, check the official sources"; }}
}});
</script></body></html>
""")

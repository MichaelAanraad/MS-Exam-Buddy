# GH-900: audience and exam-specific rules

Audience (foundational level, from the study guide): anyone who wants to show
foundational knowledge of GitHub and its core features: non-developers,
developers and all GitHub users. Covers Git, repositories, collaboration
tools, project management, modern development practices (Actions, Copilot,
Codespaces), security and administration, and the open-source community.
No prior certification is required.

- **Depth:** foundations. Test what a feature is, when to use it and how it
  differs from a neighbouring feature. No deep configuration syntax. Little or no
  code; if a snippet is needed (a Git command, a Markdown snippet, a workflow
  fragment) it must be short and verified in the documentation.
- **Products and names (current):** GitHub Free, Team, Enterprise Cloud;
  Enterprise Managed Users (EMUs); GitHub Copilot Free, Pro, Pro+, Business,
  Enterprise (plan names change; prefer concepts over plan details unless the
  study guide names them: Individuals, Business, Enterprise); Copilot agents
  and Agent Mode; GitHub Actions; GitHub Codespaces; github.dev; GitHub Pages;
  GitHub Projects; GitHub Discussions; GitHub Sponsors; GitHub Marketplace;
  InnerSource; passkeys and two-factor authentication (2FA).
- **Language:** English. No programming-language rule applies.
- **References:** `ref` is a page you actually saw, on `https://docs.github.com/`
  or `https://learn.microsoft.com/` (see `REF_PREFIXES` in `objectives.py`).
- **Imported-style explanations:** this exam has one `explanation` per question
  and no per-choice `rationale` (`IMPORTED_SINGLE_EXPLANATION = True`). Only
  `single` and `multi` types are used. The explanation names the correct choice
  and says briefly why the strongest distractors do not fit.
- Treat Microsoft Learn's study guide as the scope: do not test anything that is
  not in the skills measured.

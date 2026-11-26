# CCDV-F: audience and exam-specific rules

Audience (foundations level): a developer who builds applications and agents on
Claude. Works with the Claude API (Messages API, tools, streaming, vision,
extended thinking, prompt caching, Batches API), the Claude Agent SDK, Claude
Code, and the Model Context Protocol (MCP), and may reach Claude through Amazon
Bedrock or Google Vertex AI. Uses everyday software-engineering practice:
REST, JSON, async code, version control, code review.

**Source of the objectives:** Anthropic does not publish a free study guide for
this exam. The eight domains and their weights come from two third-party
write-ups that agree with each other (Agents & Workflows 14.7%, Applications &
Integration 33.1%, Claude Code 3.1%, Evaluation, Testing & Debugging 2.6%,
Model Selection & Optimization 16.8%, Prompt & Context Engineering 11%,
Security & Safety 8.1%, Tools & MCPs 10.6%). The objective wording in
`objectives.py` is a paraphrase of their domain descriptions, not an official
text. The two smallest domains get a few more questions than their weight so
that each has some coverage.

- **Depth:** foundations. Test design decisions and concepts: when to use a
  workflow vs an agent, which model tier, how caching or batching changes cost,
  how to scope a tool, how to resist prompt injection. Prefer concepts that are
  stable over exact parameter names or model version strings; refer to model
  tiers (Opus, Sonnet, Haiku) rather than specific versions.
- **Code language:** Python only. Short snippets are allowed only when verified
  in the documentation (Claude API, Agent SDK, MCP). No C#/.NET, no other
  languages.
- **Products and names (current):** Claude API, Messages API, Claude Agent SDK,
  Claude Code (CLAUDE.md, settings.json, skills, slash commands, subagents,
  hooks, headless mode), Model Context Protocol (MCP) with stdio and remote
  transports, Amazon Bedrock, Google Vertex AI, Batches API, prompt caching.
- **References:** `ref` is a page you actually saw on one of the documentation
  sites listed in `REF_PREFIXES` in `objectives.py`. Never invent a URL.
- **Imported-style explanations:** this exam has one `explanation` per question
  and no per-choice `rationale` (`IMPORTED_SINGLE_EXPLANATION = True`). Only
  `single` and `multi` types are used. The explanation names the correct choice
  and says briefly why the strongest distractors do not fit.

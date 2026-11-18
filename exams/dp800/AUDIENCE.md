# DP-800: audience and exam-specific rules

Audience (from the study guide): a database developer who designs and builds
AI-enabled database solutions on Microsoft SQL Server, Azure SQL and SQL
databases in Microsoft Fabric. Writes T-SQL, works with structured and
semi-structured (JSON) data, knows CI/CD in GitHub, understands AI concepts
(embeddings, vectors, models), and works with application developers, DBAs,
architects, AI engineers, DevSecOps engineers and security administrators.

- **Code language:** T-SQL for every database object, query and procedure.
  Data API builder configuration is JSON (`dab-config.json`). GitHub Copilot
  instruction files are Markdown (`.github/copilot-instructions.md`,
  `.instructions.md`). CI/CD examples use GitHub Actions YAML. No Python, no
  C#, no .NET. Do not invent T-SQL syntax: every statement, function and
  option must be verified on Microsoft Learn.
- **Platforms:** name the platform in the stem when it matters: SQL Server
  2025 (17.x), SQL Server 2022 (16.x), Azure SQL Database, Azure SQL Managed
  Instance, SQL database in Microsoft Fabric. Many features differ by platform
  (for example the native json type and JSON indexes are on SQL Server 2025,
  Azure SQL and Fabric SQL database, and graph and ledger features differ per
  platform), so a platform is a good buried constraint.
- **Product names:** Microsoft SQL Server, Azure SQL Database, Azure SQL
  Managed Instance, SQL database in Microsoft Fabric, Microsoft Fabric
  (lakehouse, OneLake), Microsoft Foundry, GitHub Copilot, Microsoft Copilot
  in Fabric, Data API builder (DAB), SQL Database Projects (SDK-style), Azure
  Functions (SQL trigger binding), Azure Logic Apps, Azure Monitor,
  Application Insights, Log Analytics, Managed Identity, Microsoft Entra ID.
  Use current names. Do not use "Azure AI Foundry" or "Azure SQL Data Warehouse".
- **Preview features:** most questions cover generally available features. A
  preview feature may appear only when it is commonly used, and then the stem
  must say it is a preview feature. Check the feature status on Learn.
- **Least privilege:** in security questions the key is the narrowest control
  that meets the stated requirement (for example a column-level permission
  rather than a database role, or passwordless Managed Identity rather than a
  stored secret). Broader controls are the distractors.
- **Performance questions:** name the evidence the stem provides (an execution
  plan, Query Store output, a DMV result, a blocking chain). Do not write
  questions that only a benchmark can settle.
- **AI questions:** test design choices with stated constraints (cost, latency,
  language, data size, freshness, security). Model names and quotas change
  often; do not test exact model names or quota numbers unless a Learn page you
  fetched states them.
- **Scope of the study guide:** test only the sub-objectives listed in
  `objectives.py`. Items such as Python, Azure AI services SDKs or C# are out
  of scope.
- **New features** (vector data type and functions, hybrid search, reciprocal
  rank fusion, DAB, GitHub Copilot instruction files): test only what a Learn
  page you fetched describes. If Learn has little on a sub-topic, write fewer
  hard questions on it rather than inventing settings, and say so in your
  report.

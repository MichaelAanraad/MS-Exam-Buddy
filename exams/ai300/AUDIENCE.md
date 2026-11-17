# AI-300: audience and exam-specific rules

Audience (associate level, from the study guide): a data scientist or ML
engineer who sets up infrastructure for MLOps and GenAIOps on Azure ("AI
operations"). Trains, optimizes, deploys and maintains traditional machine
learning models with Azure Machine Learning, and deploys, evaluates, monitors
and optimizes generative AI applications and agents with Microsoft Foundry.
Programs in Python and has an entry-level understanding of DevOps: GitHub
Actions, command-line interfaces, infrastructure as code with Bicep and the
Azure CLI. Works with data scientists, DevOps teams and stakeholders.

- **Depth:** associate = implementer. Test how to do it: SDK and CLI calls,
  YAML job and endpoint specs, configuration choices, troubleshooting a failed
  job or endpoint, the order of provisioning steps. Not strategy or adoption.
- **Code language:** Python only, no C#/.NET. Azure Machine Learning Python
  SDK v2 (`azure-ai-ml`: `MLClient`, `command`, `Environment`, `Model`,
  `ManagedOnlineEndpoint`, ...), MLflow (`mlflow.log_metric`,
  `mlflow.register_model`, ...), and the Foundry SDKs where Learn shows them.
  Commands: Azure CLI with the `ml` extension (CLI v2: `az ml workspace create`,
  `az ml job create`, `az ml online-deployment update`, ...), `az deployment
  group create` with Bicep, `az cognitiveservices` where Learn uses it for
  Foundry resources, GitHub Actions workflow YAML, `git`. Azure Machine Learning
  YAML (CLI v2 schemas) is fine inside a fenced block.
- **Version rule:** v2 only. SDK v1 (`azureml-core`) and CLI v1 (`azure-cli-ml`)
  may appear as distractors only when the rationale says they are the older,
  deprecated version. Check Learn for retirement notices before testing any
  feature (for example prompt flow, hub-based projects, classic monitoring).
- **Product names:** Microsoft Foundry (not Azure AI Foundry or Azure AI
  Studio), Foundry projects and Foundry resources, Foundry Models, Foundry
  Agent Service, Azure Machine Learning (workspace, registries, compute
  instances and clusters, managed online endpoints, batch endpoints, model
  monitoring), Microsoft Entra ID (not Azure AD), managed identities, Azure
  Monitor and Application Insights, Azure AI Search, Azure Key Vault, Azure
  Container Registry, Azure Private Link, provisioned throughput units (PTU).
- **Least privilege:** in RBAC questions the key is the narrowest built-in role
  that does the job (for example AzureML Data Scientist, AzureML Compute
  Operator, Azure AI User, Azure AI Developer, Cognitive Services OpenAI User).
  Verify every role name and what it allows on Learn; roles change.
- **Two platforms:** domains 1-2 are Azure Machine Learning; domains 3-5 are
  mainly Microsoft Foundry. Keep each question on the platform its objective
  names; a neighbouring-platform feature is a good distractor.
- **New or preview features:** the exam may include commonly used preview
  features. Test only what a Learn page you fetched describes. If Learn has
  little on a sub-topic, write fewer hard questions on it rather than inventing
  settings, and say so in your report.

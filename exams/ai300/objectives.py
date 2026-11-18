# Change these lines (plus DOMAINS and GROUPS) to build a practice exam for another certification.
EXAM = "AI-300"
EXAM_TITLE = "Operationalizing Machine Learning and Generative AI Solutions"
STUDY_GUIDE = "https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-300"
# GitHub Actions and the GitHub integration are in the study guide, so refs may also come from GitHub Docs.
REF_PREFIXES = ("https://learn.microsoft.com/", "https://docs.github.com/")

# Source: STUDY_GUIDE (fetched 2026-11-17)
# Allocation: D1 95 (19%), D2 149 (29.8%), D3 122 (24.4%), D4 67 (13.4%), D5 67 (13.4%) = 500,
# midpoints of the official weight ranges (17.5 / 27.5 / 22.5 / 12.5 / 12.5), normalized.
DOMAINS = {
    "1": ("Design and implement an MLOps infrastructure", "15-20%"),
    "2": ("Implement machine learning model lifecycle and operations", "25-30%"),
    "3": ("Design and implement a GenAIOps infrastructure", "20-25%"),
    "4": ("Implement generative AI quality assurance and observability", "10-15%"),
    "5": ("Optimize generative AI systems and model performance", "10-15%"),
}
# group id: (title, questions per objective, objectives)
GROUPS = {
    "1.1": ("Create and manage resources in a Machine Learning workspace", 7, [
        "Create and manage a workspace",
        "Create and manage datastores",
        "Create and manage compute targets",
        "Configure identity and access management for workspaces"]),
    "1.2": ("Create and manage assets in a Machine Learning workspace", 7, [
        "Create and manage data assets",
        "Create and manage environments",
        "Create and manage components",
        "Share assets across workspaces by using registries"]),
    "1.3": ("Implement IaC for Machine Learning", 8, [
        "Configure GitHub integration with Machine Learning to enable secure access",
        "Deploy Machine Learning workspaces and resources by using Bicep and Azure CLI",
        "Automate resource provisioning by using GitHub Actions workflows",
        "Restrict network access to Machine Learning workspaces",
        "Manage source control for machine learning projects by using Git"]),
    "2.1": ("Orchestrate model training", 8, [
        "Configure experiment tracking with MLflow",
        "Use automated machine learning to explore optimal models",
        "Use notebooks for experimentation and exploration",
        "Automate hyperparameter tuning",
        "Run model training scripts",
        "Manage distributed training for large and deep learning models",
        "Implement training pipelines",
        "Compare model performance across jobs"]),
    "2.2": ("Implement model registration and versioning", 8, [
        "Package a feature retrieval specification with the model artifact",
        "Register an MLflow model",
        "Evaluate a model by using responsible AI principles",
        "Manage model lifecycle, including archiving models"]),
    "2.3": ("Deploy machine learning models for production environments", 9, [
        "Deploy models as real-time or batch endpoints with managed inference options",
        "Test and troubleshoot model endpoints",
        "Implement progressive rollout and safe rollback strategies"]),
    "2.4": ("Monitor and maintain machine learning models in production", 9, [
        "Detect and analyze data drift",
        "Monitor performance metrics of models deployed to production",
        "Configure retraining or alert triggers when thresholds are exceeded"]),
    "3.1": ("Implement Foundry environments and platform configuration", 11, [
        "Create and configure Foundry resources and project environments",
        "Configure identity and access management with managed identities and role-based access control (RBAC)",
        "Implement network security and private networking configurations",
        "Deploy infrastructure using Bicep templates and Azure CLI"]),
    "3.2": ("Deploy and manage foundation models for production workloads", 11, [
        "Deploy foundation models by using serverless API endpoints and managed compute options",
        "Select appropriate models for specific use cases",
        "Implement model versioning and production deployment strategies",
        "Configure provisioned throughput units for high-volume workloads"]),
    "3.3": ("Implement prompt versioning and management with source control", 11, [
        "Design and develop prompts",
        "Create prompt variants and compare performance across different prompts",
        "Implement version control for prompts by using Git repositories"]),
    "4.1": ("Configure evaluation and validation for generative AI applications and agents", 9, [
        "Create test datasets and data mapping for comprehensive model evaluation",
        "Implement AI quality metrics, including groundedness, relevance, coherence, and fluency",
        "Configure risk and safety evaluations for harmful content detection",
        "Set up automated evaluation workflows by using built-in and custom evaluation metrics"]),
    "4.2": ("Implement observability for generative AI applications and agents", 8, [
        "Examine continuous monitoring in Foundry",
        "Monitor performance metrics, including latency, throughput, and response times",
        "Track and optimize cost metrics, including token consumption and resource usage",
        "Configure detailed logging, tracing, and debugging capabilities for production troubleshooting"]),
    "5.1": ("Optimize retrieval-augmented generation (RAG) performance and accuracy", 9, [
        "Optimize retrieval performance by tuning similarity thresholds, chunk sizes, and retrieval strategies",
        "Select and fine-tune embedding models for domain-specific use cases and accuracy improvements",
        "Implement and optimize hybrid search approaches combining semantic and keyword-based retrieval",
        "Evaluate and improve RAG system performance by using relevance metrics and A/B testing frameworks"]),
    "5.2": ("Implement advanced fine-tuning and model customization", 8, [
        "Design and implement advanced fine-tuning methods",
        "Create and manage synthetic data for fine-tuning",
        "Monitor and optimize fine-tuned model performance",
        "Manage a fine-tuned model from development through production deployment"]),
}
TOTAL = 500  # question bank size; validate.py and build.py check against it
# Exceptions to the per-group count so the total is exactly TOTAL and each domain hits its allocation.
OVERRIDE = {"1.3.5": 7, "2.1.3": 7, "3.2.1": 12, "4.2.1": 7, "5.2.2": 7}


def objectives():
    """{objective id: (text, target count)}"""
    out = {}
    for g, (_, n, objs) in GROUPS.items():
        for i, text in enumerate(objs, 1):
            oid = f"{g}.{i}"
            out[oid] = (text, OVERRIDE.get(oid, n))
    return out


if __name__ == "__main__":
    o = objectives()
    by_dom = {d: sum(n for k, (_, n) in o.items() if k[0] == d) for d in DOMAINS}
    print(len(o), "objectives,", sum(n for _, n in o.values()), "questions", by_dom)
    assert sum(n for _, n in o.values()) == TOTAL
    for g, (title, n, objs) in GROUPS.items():
        print(g, title, [o[f"{g}.{i}"][1] for i in range(1, len(objs) + 1)])

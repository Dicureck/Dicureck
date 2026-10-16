# Engineering Labs | Reproducible Software Demonstrations

The profile repository contains three original, independent sample projects alongside its documented SQL, analytics and quality repositories.

| Lab | Functionality | Current verification |
|---|---|---|
| [AI & Business Automation](ai-business-automation/README.md) | Python synthetic reports, HTML, JSON, **unsent** .eml preview, optional approval-gated OpenAI/Anthropic review | Python offline tests in CI; provider calls not exercised |
| [Enterprise BI & Reporting](enterprise-bi-reporting/README.md) | Shared 72-row fictional dataset, Python/HTML KPIs, matching T-SQL, parameterized RDL and calculation contracts for Power BI/Tableau | 14 offline checks plus [real SQL Server CI](https://github.com/Dicureck/Dicureck/actions/runs/38917647482); SSRS/Power BI/Tableau runtimes untested |
| [Enterprise Reporting & C#](enterprise-reporting-dotnet/README.md) | .NET 8 typed fictional CSV input, validation, decimal summaries and JSON report | GitHub Actions builds, self-tests and produces output |

**Case studies:** [Enterprise BI](../case-studies/enterprise-bi-reporting.md) · [Automation and AI](../case-studies/ai-automation.md) · [C# reporting](../case-studies/enterprise-reporting.md).

**Release preparation:** [AI Automation v0.1.0 draft](ai-business-automation/RELEASE_NOTES_DRAFT.md) · [.NET Reporting v0.1.0 draft](enterprise-reporting-dotnet/RELEASE_NOTES_DRAFT.md). These are **not** separate native GitHub Releases.

**No real customer data or production integrations.** Separate top-level GitHub repos are not created by this folder structure. The original RDL definition is now available; native SSRS, Power BI and Tableau runtime validation is still a future step.

[Portfolio](https://dicureck.github.io/) · [BI examples](../knowledge-base/bi-examples.md) · [All documentation](../knowledge-base/README.md)

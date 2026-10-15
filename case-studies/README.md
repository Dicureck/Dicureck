# Engineering Case Studies

**Independent, synthetic portfolio demonstrations**. These studies describe decisions and validation boundaries without claiming employer outcomes, client endorsements or measured production improvements.

| Study | Interactive demo | Related code |
|---|---|---|
| [Route Intelligence](logistics.md) | [Explore routes](https://dicureck.github.io/?demo=logistics#lab) | [Logistics lab](https://github.com/Dicureck/logistics-route-intelligence) |
| [Financial Intelligence](finance.md) | [Explore finance](https://dicureck.github.io/?demo=finance#lab) | [Financial lab](https://github.com/Dicureck/financial-intelligence-lab) |
| [Incident Intelligence](incidents.md) | [Explore incidents](https://dicureck.github.io/?demo=incidents#lab) | [Incidents lab](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales) |

## Software and automation studies

| Study | Published implementation | Verification boundary |
|---|---|---|
| [AI & Business Automation](ai-automation.md) | [Python source](../engineering-labs/ai-business-automation/README.md) | Offline tests; no real emails |
| [Enterprise BI & Reporting](enterprise-bi-reporting.md) | [72-row Python/SQL/RDL/DAX lab](../engineering-labs/enterprise-bi-reporting/README.md) | Source-consistent inputs and XML tests; native BI runtimes pending |
| [Enterprise Reporting & C#](enterprise-reporting.md) | [.NET 8 source](../engineering-labs/enterprise-reporting-dotnet/README.md) | CI build and synthetic JSON |

The interactive website generates a deterministic local sample. The corresponding repository projects may use separate independently generated synthetic fixtures. **Numbers and outputs are not claimed to match across independent demos unless a specific reconciliation test has been run.**

## How to read a study

Each follows a consistent engineering narrative: **question → data contract → design → validation → limitations → demo**. Screenshots should always be labeled with synthetic sample and software version. No internal screenshots, system endpoints or actual business data are included.

[Engineering Knowledge Base](../knowledge-base/README.md) · [Portfolio](https://dicureck.github.io/)


## Verified SQL Server case-study evidence

The [SQL Performance Lab](https://github.com/Dicureck/sql-performance-lab/blob/main/docs/verified-ci-benchmark-2026-10-15.md) has a real SQL Server Developer container run with synthetic fixtures, duplicate-aware result equivalence and measured smoke timings. The observations are bounded to one CI environment.

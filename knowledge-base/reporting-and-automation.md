# Reporting, Software & AI Automation | Engineering Roadmap

This page distinguishes **published, verifiable examples** from **planned demonstrations**.

## Currently available

| Public artifact | Evidence | Scope |
|---|---|---|
| [SQL Performance Lab](https://github.com/Dicureck/sql-performance-lab) | Source, tests, benchmark harness | Actual SQL Server benchmark measurements remain a separate validation step |
| [Oracle Migration Toolkit](https://github.com/Dicureck/oracle-migration-toolkit) | Scanner, planner, offline checks, tests | No live cross-engine parity claim |
| [Logistics lab](https://github.com/Dicureck/logistics-route-intelligence) | Python, synthetic dataset, offline dashboard | No client KPIs |
| [Financial lab](https://github.com/Dicureck/financial-intelligence-lab) | Synthetic P&L, tests and dashboard | Not accounting advice |
| [Incident lab](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales) | Synthetic SLA/backlog dashboard | Not a production incident monitoring service |
| [Data Quality Toolkit](https://github.com/Dicureck/data-quality-toolkit) | CLI and deterministic fixtures | Specific offline data contracts |

## Reference engineering guides

- [Power BI, Tableau, SSRS / Report Builder and Crystal Reports](reporting-platforms.md)
- [Python & pandas](python-pandas.md)
- [C# / .NET reporting architecture](csharp-dotnet.md)
- [Responsible AI-assisted development and mail automation](ai-automation.md)
- [Analytics Engineering](analytics-engineering.md)

## Proposed public demonstrations

**Phase 1: Native BI assets** — synthetic Power BI model, an authorized Tableau Public workbook where feasible, and example paginated reports. Validate exported numbers against source.

**Phase 2: .NET / C# CLI** — safe parsing, typed records, JSON outputs and unit tests on dummy data.

**Phase 3: AI & business automation** — synthetic report generation, mock email delivery, explicit approval gate and separate provider integrations only if safe and authorized.

These items are **planned**, not completed repositories. The existence of knowledge-base notes does not imply a shipped service or integration.

## Publication rules

Original source and data only. Never publish proprietary report templates, customer prompts, real recipients, database credentials or production measurements without proper rights and approval.

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*

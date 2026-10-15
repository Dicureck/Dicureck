# Engineering Portfolio Roadmap

Public source code and synthetic tests demonstrate concrete techniques. They are not claims of production deployments or client endorsements.

## Published work

| Project | Current public evidence | Still worth validating |
|---|---|---|
| [SQL Performance Lab](https://github.com/Dicureck/sql-performance-lab) | T-SQL cases, offline tests, benchmark harness | Actual SQL Server runtime measurements |
| [Oracle Migration Toolkit](https://github.com/Dicureck/oracle-migration-toolkit) | Offline review, dependency plan, original samples | Cross-engine integration and behavioral parity |
| [Logistics & Route Intelligence](https://github.com/Dicureck/logistics-route-intelligence) | Synthetic dataset generator, KPI dashboard, tests | Native BI artifact if added |
| [Financial Intelligence Lab](https://github.com/Dicureck/financial-intelligence-lab) | Fictional ledger/reporting, checks, dashboard | Native BI report if added |
| [Data Quality Toolkit](https://github.com/Dicureck/data-quality-toolkit) | Validation CLI, fixtures, tests | Broader schemas and adapters |
| [Operational Incident Intelligence](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales) | Synthetic incident reporting, tests | Expanded visual analysis |
| [Secret Friend](https://github.com/Dicureck/challenge-amigo-secreto-esp_main) | Browser-based JavaScript example | Accessibility and UX review |
| [Interactive Portfolio](https://dicureck.github.io/) | Published responsive site and illustrative lab dashboards | Continuous accessibility and device QA |

## Next priorities

1. Publish navigable documentation and check internal links.
2. Add SQL Server reproducible benchmark evidence, keeping test limitations explicit.
3. Produce original Tableau / Power BI / paginated reporting examples where tool licenses allow.
4. Build a .NET CLI with synthetic reports and actual automated tests.
5. Build approval-gated, dry-run-first AI and email automation examples.
6. Keep the professional portfolio and Wiki references synchronized.

The native GitHub Wiki is separate from the repository. These version-controlled pages are the canonical documents; copying a page into the Wiki does **not** create automatic synchronization.

## Release quality gate

- [ ] License and provenance checked
- [ ] Original synthetic test data only
- [ ] README setup and examples reproducible
- [ ] Published claims supported by tests
- [ ] No credentials or customer-specific records
- [ ] Link and accessibility review complete

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*

## Public engineering backlog

These issues are the trackable implementation and verification gates for the next portfolio phase. Opening an issue means the work is **planned**, not finished.

- [SQL Server runtime benchmark validation](https://github.com/Dicureck/Dicureck/issues/7)
- [Oracle cross-engine integration](https://github.com/Dicureck/Dicureck/issues/9)
- [Native reporting assets and case studies](https://github.com/Dicureck/Dicureck/issues/8)
- [Native Wiki synchronization and public Projects board](https://github.com/Dicureck/Dicureck/issues/10)

**Note:** The AI Business Automation Lab and Enterprise Reporting .NET code are currently housed in the profile repository's [engineering-labs](https://github.com/Dicureck/Dicureck/tree/main/engineering-labs) directory. Their offline CI checks are distinct from live provider, email, database and proprietary reporting product integrations.

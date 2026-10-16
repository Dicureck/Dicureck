# Engineering Portfolio Roadmap

Public source code and synthetic tests demonstrate concrete techniques. They are not claims of production deployments or client endorsements.

## Published work

| Project | Current public evidence | Still worth validating |
|---|---|---|
| [SQL Performance Lab](https://github.com/Dicureck/sql-performance-lab) | **SQL Server Developer CI validated:** full-row equivalence, [actual plans / CPU / logical reads](https://github.com/Dicureck/sql-performance-lab/blob/main/docs/verified-deep-profile-2026-10-16.md) across three selectivity runners, and [permanent raw evidence](https://github.com/Dicureck/sql-performance-lab/tree/main/evidence/deep-profiles/ci-38943948019) | More independent repeats of identical windows, higher cardinalities and production-like concurrency remain future research |
| [Oracle Migration Toolkit](https://github.com/Dicureck/oracle-migration-toolkit) | Offline toolkit CI plus [real Oracle Free 26ai syntax and query smoke](https://github.com/Dicureck/oracle-migration-toolkit/blob/main/evidence/oracle-free-runtime-2026-10-15.json) | **Oracle 12.1** compatibility and SQL Server ↔ Oracle functional parity |
| [Logistics & Route Intelligence](https://github.com/Dicureck/logistics-route-intelligence) | Synthetic dataset generator, KPI dashboard, tests | Native BI artifact if added |
| [Financial Intelligence Lab](https://github.com/Dicureck/financial-intelligence-lab) | Fictional ledger/reporting, checks, dashboard | Native BI report if added |
| [Data Quality Toolkit](https://github.com/Dicureck/data-quality-toolkit) | Validation CLI, fixtures, tests | Broader schemas and adapters |
| [Operational Incident Intelligence](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales) | Synthetic incident reporting, tests | Expanded visual analysis |
| [Secret Friend](https://github.com/Dicureck/challenge-amigo-secreto-esp_main) | Browser-based JavaScript example | Accessibility and UX review |
| [Interactive Portfolio](https://dicureck.github.io/) | Published responsive site and illustrative lab dashboards | Continuous accessibility and device QA |

## Next priorities

1. **Completed:** [deeper SQL Server benchmarking](https://github.com/Dicureck/sql-performance-lab/blob/main/docs/verified-deep-profile-2026-10-16.md) with server CPU, logical reads, 12 real plans, three independent runners with *different* date-window selectivities and seven within-run trials. Further identical-window cross-run sampling remains optional future research.
2. Verify the offline Oracle toolkit against controlled Oracle and SQL Server engines.
3. Expand the [new Enterprise BI Lab](../engineering-labs/enterprise-bi-reporting/README.md): original parameterized RDL and identical fictional Python/SQL/DAX/Tableau data contracts exist; the [TMDL semantic model source](../engineering-labs/enterprise-bi-reporting/powerbi/EnterpriseSales.SemanticModel/README.md) and static checks are prepared; validate native Report Builder, Power BI Desktop and Tableau runtimes with reconciled exports.
4. Extend the existing runnable [Python automation](../engineering-labs/ai-business-automation/README.md) and [.NET 8 reporting](../engineering-labs/enterprise-reporting-dotnet/README.md) laboratories with more fixtures and presentation assets.
5. Prepare official GitHub Releases from evidence-backed draft notes (a draft is **not** a native release).
6. Maintain the [synchronized native Wiki](https://github.com/Dicureck/Dicureck/wiki) and [public Engineering Board](https://github.com/users/Dicureck/projects/1/views/2).

The native Wiki is a separate Git repository. Eight curated pages are now synchronized from the controlled wiki-pages directory via GitHub Actions; the hand-authored Home and SQL Performance pages remain protected. The detailed knowledge-base documents are not mirrored verbatim.

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
- [Native GitHub Releases from verified source and change logs](https://github.com/Dicureck/Dicureck/issues/11)

**Note:** The AI Business Automation Lab and Enterprise Reporting .NET code are currently housed in the profile repository's [engineering-labs](https://github.com/Dicureck/Dicureck/tree/main/engineering-labs) directory. Their offline CI checks are distinct from live provider, email, database and proprietary reporting product integrations.


## Public overview and screenshot evidence

The [responsive public development roadmap](https://dicureck.github.io/roadmap.html) summarizes verified and planned work. Actual Chromium screenshots from the successful [live-site run](https://github.com/Dicureck/dicureck.github.io/actions/runs/38812402350) are available as a GitHub Actions artifact; source data are entirely fictional.

[Release readiness by repository](releases.md) lists source version, CI evidence and outstanding native GitHub release steps.


## Six official GitHub Releases

All six standalone source laboratories now provide [official v0.1.0 GitHub Releases](releases.md). Each release has passed its repository's CI for the exact tagged commit; see its page for evidence and limitations. AI/automation and .NET reporting remain subfolders in the profile repository.

The native [Engineering Board](https://github.com/users/Dicureck/projects/1/views/2) is public and configured with five linked Issues. The [Wiki Sync workflow](https://github.com/Dicureck/Dicureck/actions/workflows/wiki-sync.yml) now maintains eight curated internal tutorials.

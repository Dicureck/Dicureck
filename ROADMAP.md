# Public Engineering Roadmap

## Shipped / source available
- [x] [Portfolio website](https://dicureck.github.io/) with synthetic interactive logistics, finance and incidents dashboards
- [x] Deep-linkable dashboards for sharing from individual GitHub repositories
- [x] [Three technical case studies](case-studies/README.md)
- [x] [Python automation lab](engineering-labs/ai-business-automation/README.md) with offline tests, dry-run email previews and guarded provider adapters
- [x] [.NET reporting lab](engineering-labs/enterprise-reporting-dotnet/README.md) with source, CSV input validation and CI
- [x] [Reporting platform calculation notes](knowledge-base/bi-examples.md)
- [x] [Unified Enterprise BI Reporting Lab](engineering-labs/enterprise-bi-reporting/README.md), with one 72-row source dataset, report JSON/HTML, SQL fixture, original RDL and DAX/Tableau calculation contracts
- [x] [Execute the actual Enterprise BI RDL query against real SQL Server Developer](https://github.com/Dicureck/Dicureck/actions/runs/38917647482), verify all 72 source records and exact groups/decimals for three date windows

## Official v0.1.0 source releases

Six independent repositories now have [official tagged releases](knowledge-base/releases.md), with GitHub Actions checks, original fixtures and clearly stated limitations.

## Next verification gates
- [ ] Test optional OpenAI / Anthropic APIs in a controlled non-production account; never store provider keys or live responses in the public repo
- [x] Run initial real SQL Server Developer CI benchmark with synthetic fixtures and [publish bounded measurements](https://github.com/Dicureck/sql-performance-lab/blob/main/docs/verified-ci-benchmark-2026-10-15.md)
- [x] Expand SQL Server benchmarks with [actual plans, server CPU, logical reads, three selectivity runners and seven trials per variant](https://github.com/Dicureck/sql-performance-lab/blob/main/docs/verified-deep-profile-2026-10-16.md), with [permanent raw evidence](https://github.com/Dicureck/sql-performance-lab/tree/main/evidence/deep-profiles/ci-38943948019) and explicit statistical limits
- [x] Execute original SQL Server ↔ Oracle Free candidate queries in separate disposable real engines with [verified 260-order source/row parity](https://github.com/Dicureck/oracle-migration-toolkit/blob/main/docs/verified-cross-engine-parity-2026-10-16.md) and [archived original results](https://github.com/Dicureck/oracle-migration-toolkit/tree/main/evidence/cross-engine/ci-38946759282); **Oracle 12.1.0.2 compatibility remains an open, separately required target test**
- [ ] Publish actual Power BI / Tableau / RDL demonstrations after runtime validation and licensing checks
- [x] Synchronize [eight native GitHub Wiki tutorials](https://github.com/Dicureck/Dicureck/wiki) with [protected GitHub Actions](https://github.com/Dicureck/Dicureck/actions/runs/38824211359), preserving the original Home and SQL Performance pages
- [x] Publish [six native GitHub Releases v0.1.0](knowledge-base/releases.md) from CI-verified source
- [x] Create the [public GitHub Engineering Board](https://github.com/users/Dicureck/projects/1)
- [x] Import existing Issues #7–#11, configure Todo / In Progress / Done statuses, and arrange them on the [public Engineering Board](https://github.com/users/Dicureck/projects/1/views/2); [board documentation](knowledge-base/projects-board-setup.md)
- [ ] Extract each monorepo engineering lab into a dedicated repository once creation is authorized/supported by tooling

Follow progress on the [native Engineering Board](https://github.com/users/Dicureck/projects/1/views/2) or through the linked [GitHub Issues](https://github.com/Dicureck/Dicureck/issues). This Markdown roadmap complements—not replaces—the board.

## Quality bar

Reproducible datasets, explicit source-level tests, exact metric contracts, no claimed production validation without evidence, documented privacy boundaries and public CI logs.

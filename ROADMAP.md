# Public Engineering Roadmap

## Shipped / source available
- [x] [Portfolio website](https://dicureck.github.io/) with synthetic interactive logistics, finance and incidents dashboards
- [x] Deep-linkable dashboards for sharing from individual GitHub repositories
- [x] [Three technical case studies](case-studies/README.md)
- [x] [Python automation lab](engineering-labs/ai-business-automation/README.md) with offline tests, dry-run email previews and guarded provider adapters
- [x] [.NET reporting lab](engineering-labs/enterprise-reporting-dotnet/README.md) with source, CSV input validation and CI
- [x] [Reporting platform calculation notes](knowledge-base/bi-examples.md)

## Next verification gates
- [ ] Test optional OpenAI / Anthropic APIs in a controlled non-production account; never store provider keys or live responses in the public repo
- [ ] Run SQL Server benchmark scripts against a dedicated local test database and publish full methodology
- [ ] Run SQL Server → Oracle comparison in authorized isolated instances and validate result multiset equivalence
- [ ] Publish actual Power BI / Tableau / RDL demonstrations after runtime validation and licensing checks
- [ ] Add native GitHub Wiki pages for expanded technical sections (separate Git repo / edit workflow)
- [ ] Publish native GitHub releases with immutable tags and attached release notes
- [ ] If GitHub Projects is enabled for this account, create a public project board linked to tracked issues
- [ ] Extract each monorepo engineering lab into a dedicated repository once creation is authorized/supported by tooling

For progress, use [GitHub Issues](https://github.com/Dicureck/Dicureck/issues) if enabled; this checklist remains the source-controlled fallback when a native GitHub Projects board is not accessible.

## Quality bar

Reproducible datasets, explicit source-level tests, exact metric contracts, no claimed production validation without evidence, documented privacy boundaries and public CI logs.

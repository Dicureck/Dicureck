# Official Engineering Releases

**Six first-party engineering laboratories have official public GitHub Releases at v0.1.0**, created after the CI checks of their exact source commit succeeded. Each tagged version has GitHub-generated source archives (ZIP/TAR.GZ), release notes and a permanent link.

## Published versions

| Laboratory | Official release | Tested capability | GitHub status |
|---|---|---|---|
| [SQL Performance](https://github.com/Dicureck/sql-performance-lab) | [v0.1.0 — published](https://github.com/Dicureck/sql-performance-lab/releases/tag/v0.1.0) | SQL Server Developer CI + bounded benchmark | **Published** |
| [Oracle Migration](https://github.com/Dicureck/oracle-migration-toolkit) | [v0.1.0 — published](https://github.com/Dicureck/oracle-migration-toolkit/releases/tag/v0.1.0) | Offline Python and Oracle Free runtime tests | **Published** |
| [Logistics](https://github.com/Dicureck/logistics-route-intelligence) | [v0.1.0 — published](https://github.com/Dicureck/logistics-route-intelligence/releases/tag/v0.1.0) | Synthetic pipeline CI | **Published** |
| [Financial Intelligence](https://github.com/Dicureck/financial-intelligence-lab) | [v0.1.0 — published](https://github.com/Dicureck/financial-intelligence-lab/releases/tag/v0.1.0) | Synthetic reporting CI | **Published** |
| [Data Quality](https://github.com/Dicureck/data-quality-toolkit) | [v0.1.0 — published](https://github.com/Dicureck/data-quality-toolkit/releases/tag/v0.1.0) | Original fixture validation CI | **Published** |
| [Incident Intelligence](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales) | [v0.1.0 — published](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales/releases/tag/v0.1.0) | Incident analytics CI | **Published** |

**Verified October 15, 2026:** all six links were retrieved from GitHub's Releases API. The Oracle release was separately gated on both the Python validation workflow and a temporary Oracle Free runtime test. The SQL Performance release was gated on real SQL Server Developer container integration and benchmark smoke testing.

## What v0.1.0 does and does not promise

- Each version is a **source release**, not a signed binary or certified production application.
- All public datasets are independent, deterministic and synthetic; no customer/company data.
- SQL Server benchmark figures describe one particular test environment, **not guaranteed speedups**.
- The Oracle runtime smoke uses Oracle Free and does **not** establish Oracle 12.1 compatibility or cross-engine SQL Server parity.
- Tableau, Crystal Reports and SSRS native assets and live AI provider/email integrations remain independent milestones.

## Version process

1. Review source/fixtures, licenses, CI and secrets.
2. Publish an immutable version label tied to the tested commit.
3. Create a native GitHub Release with bounded release notes and source archives.
4. Keep future updates in new versions rather than rewriting v0.1.0.

**Repository-level exception:** [AI Business Automation](../engineering-labs/ai-business-automation/README.md) and [Enterprise Reporting with C#](../engineering-labs/enterprise-reporting-dotnet/README.md) are folders within the special GitHub-profile repo, not standalone Releases. Their offline CI remains public.

The [portfolio website](https://dicureck.github.io/) has a versioned [changelog](https://github.com/Dicureck/dicureck.github.io/blob/main/CHANGELOG.md) and [live-site verification](https://github.com/Dicureck/dicureck.github.io/actions); its deployment is separate from these six lab source Releases.

[← Engineering roadmap](portfolio-roadmap.md) · [Public development roadmap](https://dicureck.github.io/roadmap.html) · [All documentation](README.md)

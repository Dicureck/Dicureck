# Versioning and Release Readiness

> GitHub source-package versions, Markdown change logs, and **native GitHub Releases** are different things. This index does not claim a published release where no official Release object has been created.

## Prepared source versions

| Repository | Source version | Draft and changelog | Verified evidence | Native Release |
|---|---|---|---|---|
| [SQL Performance](https://github.com/Dicureck/sql-performance-lab) | 0.1.0 | [Draft](https://github.com/Dicureck/sql-performance-lab/blob/main/RELEASE_NOTES_DRAFT.md) | [Real SQL Server CI](https://github.com/Dicureck/sql-performance-lab/actions/runs/38784723221) | Pending |
| [Oracle Migration](https://github.com/Dicureck/oracle-migration-toolkit) | 0.1.0 | [Draft](https://github.com/Dicureck/oracle-migration-toolkit/blob/main/RELEASE_NOTES_DRAFT.md) | [Offline CI](https://github.com/Dicureck/oracle-migration-toolkit/actions/runs/38787268146) | Pending |
| [Logistics](https://github.com/Dicureck/logistics-route-intelligence) | 0.1.0 | [Draft](https://github.com/Dicureck/logistics-route-intelligence/blob/main/RELEASE_NOTES_DRAFT.md) | [CI](https://github.com/Dicureck/logistics-route-intelligence/actions/runs/38811230456) | Pending |
| [Financial Intelligence](https://github.com/Dicureck/financial-intelligence-lab) | 0.1.0 | [Draft](https://github.com/Dicureck/financial-intelligence-lab/blob/main/RELEASE_NOTES_DRAFT.md) | [CI](https://github.com/Dicureck/financial-intelligence-lab/actions/runs/38811223504) | Pending |
| [Data Quality](https://github.com/Dicureck/data-quality-toolkit) | 0.1.0 | [Draft](https://github.com/Dicureck/data-quality-toolkit/blob/main/RELEASE_NOTES_DRAFT.md) | [CI](https://github.com/Dicureck/data-quality-toolkit/actions/runs/38792471650) | Pending |
| [Incident Intelligence](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales) | 0.1.0 | [Draft](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales/blob/main/RELEASE_NOTES_DRAFT.md) | [CI](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales/actions/runs/38811234453) | Pending |

The portfolio website itself has a [CHANGELOG](https://github.com/Dicureck/dicureck.github.io/blob/main/CHANGELOG.md) and its [live deployment checks](https://github.com/Dicureck/dicureck.github.io/actions). It too requires a separate authorized action to create a native release.

## Native release publication checklist

1. Choose a final commit SHA after clean CI tests and license review.
2. Confirm fixtures, generated screenshots and any binaries are safe and reproducible.
3. Create a signed/annotated version tag when supported, and publish through the GitHub Release interface.
4. Include actual test links, numeric evidence with context and deployment limitations.
5. Verify download links and displayed source version.

The connected GitHub actions available for this portfolio can update repository content and CI workflows but **cannot currently create the native Release object or a public GitHub Projects board**. Preparation therefore stays clearly labeled until such authorization is available.

[← Engineering roadmap](portfolio-roadmap.md) · [All documentation](README.md)

# Enterprise BI & Reporting Lab

**Python · SQL Server · SSRS / Report Builder RDL · Power BI DAX · Tableau calculations**

> An original, cohesive reporting demonstration using **one shared 72-order fictional dataset**. The runnable Python/HTML pipeline is independent of proprietary applications; native report definitions and analytical formulas are provided without claiming untested runtime support.

## Explore the original outputs

From the **Dicureck/Dicureck repository root**:

~~~bash
python engineering-labs/enterprise-bi-reporting/src/report.py \
  --input engineering-labs/enterprise-bi-reporting/fixtures/sales.csv \
  --out output/enterprise-bi

python -m unittest discover -s engineering-labs/enterprise-bi-reporting/tests -v
~~~

Open the generated **output/enterprise-bi/dashboard.html** in a browser. Filter by Region to recompute Orders, Revenue, Margin % and Budget Variance; observe interactive monthly bars and regional totals. The generator also writes **report.json**, which can be reconciled independently.

The dashboard is a static offline file, not a public live-API integration. No credentials, user records or external network calls are needed.

## Lab layout

| Artifact | Use | Validation status |
|---|---|---|
| [sales.csv](fixtures/sales.csv) | 72 original fictional order-grain records, four months | Source data, strict Python validation and tests |
| [Python reporting generator](src/report.py) | JSON, accessible local dashboard and region filters | CI unit/integration checks (when green) |
| [SQL Server schema and fixture](sql/schema.sql), [seed](sql/seed.sql), [query](sql/report.sql) | Matching SQL Server dataset, safe empty-table guard, half-open date filtering | **Real SQL Server 2022 Developer CI approved**: 72 exact source rows, 12 full-period groups, 6 subset groups and empty range; [raw evidence](evidence/sqlserver-ci-2026-10-16.json). SSRS rendering untested |
| [Native RDL file](rdl/Enterprise-Sales-Summary.rdl) | Parameterized monthly × regional paginated table; integrated Windows auth to *localhost* | XML syntax and query/field consistency checks only; **SSRS/Report Builder rendering not yet performed** |
| [Power BI semantic model TMDL](powerbi/EnterpriseSales.SemanticModel/README.md) | Source-controlled seven-column fact table, eight DAX measures and local fictional CSV import | Parsed by **Microsoft Analysis Services TOM** ([CI](https://github.com/Dicureck/Dicureck/actions/runs/38919301738)); **not opened or refreshed in Power BI Desktop** |
| [Power BI DAX](powerbi/measures.dax) | Eight additive/rate measures defined on the same fixture | Formula/source review; no validated .pbix file |
| [Tableau calculations](tableau/calculations.md) | Same KPIs and aggregate denominator rules | Original calculations; no validated .twb/.twbx |
| [Data dictionary](docs/data-dictionary.md), [verification plan](docs/verification.md) | Grain, precision, filters, sources and acceptance | Human-readable contract and test design |

## Verified SQL Server integration

A disposable **SQL Server 2022 Developer** instance ran the committed schema, original 72-row synthetic INSERT and the **same parameterized SQL query embedded in the RDL**. The test confirmed full-row equality and exact decimal equivalence against the Python generator across three independent date windows. The ephemeral test database was removed afterward.

[Successful CI run](https://github.com/Dicureck/Dicureck/actions/runs/38917647482) · [permanent SQL Server CI evidence](evidence/sqlserver-ci-2026-10-16.json) · [re-run workflow](https://github.com/Dicureck/Dicureck/actions/workflows/enterprise-bi-sqlserver.yml).

**Boundary:** this is a real SQL Server query/data verification. It does not prove that SSRS Report Builder successfully renders, prints or exports the RDL.

## Architecture

~~~mermaid
flowchart TD
  A[One committed fictional sales.csv] --> B{Schema / key / decimal validation}
  B -->|Fail| X[Reject without generating report]
  B -->|Pass| C[Exact Python Decimal aggregation]
  C --> D[JSON source of record]
  C --> E[Local interactive HTML dashboard]
  A --> F[Equivalent SQL Server seed]
  F --> G[SQL view/query with date parameters]
  G --> H[Original SSRS RDL table definition]
  A --> I[Power BI DAX calculation examples]
  A --> J[Tableau calculated fields]
  D --> K[Independent cross-tool reconciliation goal]
  H --> K
  I --> K
  J --> K
~~~

**Engineering principle:** compute **Margin % = (Σ Revenue − Σ Cost) ÷ Σ Revenue**, not the mean of order-level percentages. Budget variance is **Σ Revenue − Σ Budget**. Empty denominators become NULL/blank rather than fabricated 0%.

## What this is NOT

This is not a live financial system, a tested native PBIX/Tableau workbook, an operational SSRS server, a Crystal Reports template or verified production business outcomes. All amounts are **fictional synthetic units (SU)** and should not be presented as actual currencies.

[Technical case study](../../case-studies/enterprise-bi-reporting.md) · [Public Engineering Board](https://github.com/users/Dicureck/projects/1/views/2) · [Reporting issue #8](https://github.com/Dicureck/Dicureck/issues/8)

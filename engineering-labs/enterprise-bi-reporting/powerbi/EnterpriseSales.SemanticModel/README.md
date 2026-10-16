# Power BI · TMDL Semantic Model Source

This directory supplies **original source-controlled semantic model definitions**, in the official Power BI TMDL folder style: [Microsoft guidance](https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset).

**Current verification:** the TMDL model was successfully deserialized by Microsoft's official Analysis Services Tabular serializer in [GitHub Actions](https://github.com/Dicureck/Dicureck/actions/runs/38919301738); this confirms parseable model metadata and counts of seven fields, eight measures and one partition. The CSV import and DAX formulas have **not** been executed or refreshed inside Power BI Desktop. There is no published PBIX or packaged, validated PBIP report. Do not claim otherwise.

## Inputs and semantics

The sole source is the identical [72-order synthetic CSV](../../fixtures/sales.csv) used by the Python dashboard, SQL Server tested report and Tableau formula examples.

The model defines:
- Exactly seven typed columns; one unique fictional order per row.
- Eight DAX measures with explicit display formatting.
- M import of a **local CSV file only**, not an external API.
- Automatic rejection of a fixture with an unexpected row count or duplicate order IDs.
- Correct aggregate margin ratio and null/blank behavior for zero denominators.

## Verified parser test

[Source for the .NET parser](../tmdl-validation/Program.cs) · [Successful CI](https://github.com/Dicureck/Dicureck/actions/runs/38919301738). The official Microsoft Analysis Services SDK reads this exact TMDL folder into a Tabular database object and checks the expected columns, measures and local import partition without contacting any production system.

**Boundary:** successful TMDL deserialization is not a Power BI Desktop refresh, a verified DAX calculation or a native report screenshot.

## How to use in Power BI Desktop

This folder is **TMDL model source, not a complete PBIP report**. To use it, create or open an original Power BI Desktop project in TMDL mode and import/merge this model source following Microsoft's project authoring guidance. Set the model's `SalesCsvPath` parameter to the **absolute local location of sales.csv** on your computer, then refresh and validate the metrics.

The placeholder `SET_LOCAL_PATH_TO_SYNTHETIC_SALES_CSV` deliberately cannot access a private machine: each reviewer chooses their own local file. No credential or production server is embedded.

Only after Desktop successfully opens and evaluates it should a PBIX/PBIP report and native screenshots be saved and described as tested.

## Independent reference totals

The original [Python report](../../src/report.py) and [real SQL Server CI](../../evidence/sqlserver-ci-2026-10-16.json) agree for the full fixture:

| KPI | Expected synthetic value |
|---|---:|
| Orders | 72 |
| Revenue SU | 124,344.00 |
| Cost SU | 70,536.34 |
| Margin SU | 53,807.66 |
| Margin % | 43.27% |
| Budget SU | 123,444.00 |
| Budget Variance SU | +900.00 |

Power BI's fixed-decimal import uses four decimal places internally; this sample provides amounts with two. Final native checks must still confirm filters, correct date parsing, and totals.

[Lab overview](../../README.md) · [Power BI DAX standalone examples](../measures.dax).

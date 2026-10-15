# Reporting Engineering | Power BI, Tableau, SSRS & Crystal Reports

**Status:** original platform methodology and a new [Enterprise BI Lab](../engineering-labs/enterprise-bi-reporting/README.md) now include a real **RDL source file**, a shared synthetic fixture, DAX measures and Tableau calculations. The RDL is statically validated; no Report Builder/SSRS render, Tableau workbook or Power BI PBIX has been runtime-tested.

## 01 · Choose the delivery format

| Format | Best fit | Key engineering checks |
|---|---|---|
| Power BI | Exploratory and executive BI | Model relationships, DAX, refresh, security |
| Tableau | Interactive visual analysis | Calculation grain, filters, parameter behavior |
| SSRS / Report Builder | Paginated, printable reports | Parameter defaults, pagination, export parity |
| Crystal Reports | Formatted operational reporting | Grouping/suppression, data source credentials, exports |
| HTML dashboard | Public, dependency-light demonstration | Accessible layout, synthetic data, responsive interaction |

## 02 · Before building any report

- Write a reporting contract: intended audience, dimensions, grain, and exact metric definitions.
- Confirm source authorization and credentials management.
- Define aggregation boundaries and independent reconciliation values.
- Design filter/parameter semantics and handling of missing values.
- Make export output match the agreed schema and formatting.
- Include empty-state, timeout and error behavior.

## 03 · Platform-specific considerations

**Tableau:** distinguish FIXED LOD calculations from view-level aggregates; document the order of filters and test actions that change the denominator.

**Report Builder / SSRS:** separate report parameters from SQL parameters; test PDF/Excel exports, headers, repeated groups, whitespace and print-friendly page breaks. Avoid embedding sensitive connection strings in public RDL files.

**Crystal Reports:** validate formula evaluation stages, grouping and suppression behavior, PDF layout and data source mapping; keep proprietary template files private without distribution rights.

**Power BI:** prefer reusable measures, a declared model grain and reconciliation to source; validate row-level security only with approved test identities.

## 04 · Public proof standard

An excellent portfolio artifact includes a clean, synthetic dataset, model documentation, a screenshot/video preview, original formulas, known limitations, and—when licensing allows—a runnable workbook/report.

The RDL and calculation sources are now **shipped as original examples**. Mark native render/export results as **pending** until independently tested.

Related: [Analytics Engineering](analytics-engineering.md) · [Reporting & Automation roadmap](reporting-and-automation.md).

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*

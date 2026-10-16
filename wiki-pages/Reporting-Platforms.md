# BI & Enterprise Reporting Platforms

**Power BI · Tableau · SSRS / Report Builder · Crystal Reports**

## Choose the right format

| Platform | Best fit | Evidence checks |
|---|---|---|
| Power BI | Executive and interactive analytics | DAX grain, relationship filters, security |
| Tableau | Interactive data exploration | LOD calculations and filter context |
| Report Builder / SSRS | Printable/paginated reports | Parameters, exported totals, PDF/Excel layout |
| Crystal Reports | Structured operational documents | Grouping, sections, export and credential handling |
| HTML dashboards | Public functional demonstrations | Accessible filters, synthetic data, browser tests |

A public engineering example should include a data dictionary, exact KPI definitions, original fictional fixtures, reproducible formulas, and output reconciliation.

**Current status:** the original [Enterprise BI reporting lab](https://github.com/Dicureck/Dicureck/tree/main/engineering-labs/enterprise-bi-reporting) now has an HTML dashboard and source-equivalent SQL Server, DAX, Tableau and RDL definitions. The SQL Server query ran successfully in [isolated real SQL Server CI](https://github.com/Dicureck/Dicureck/actions/runs/38917647482). **Native Report Builder rendering, Power BI/TWB execution and Crystal Reports remain separate unfinished checks.**

[Reporting guide](https://github.com/Dicureck/Dicureck/blob/main/knowledge-base/reporting-platforms.md) · [BI calculation examples](https://github.com/Dicureck/Dicureck/blob/main/knowledge-base/bi-examples.md).


---

Independent engineering demonstrations with synthetic data. [Portfolio](https://dicureck.github.io/) · [Public Projects Board](https://github.com/users/Dicureck/projects/1/views/2).

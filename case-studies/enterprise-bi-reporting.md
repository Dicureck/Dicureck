# Enterprise BI & Reporting Lab | Engineering Case Study

**Python · SQL Server · SSRS RDL · DAX · Tableau calculation contracts**

[Lab and all source files](../engineering-labs/enterprise-bi-reporting/README.md) · [14 offline tests](../engineering-labs/enterprise-bi-reporting/tests/test_report.py) · [GitHub Actions](../.github/workflows/engineering-labs.yml)

## 01 · Business question

How can a finance or operations team define a consistent set of performance indicators for regional sales, then carry those definitions between an interactive dashboard and multiple reporting tools without changing the denominators?

This is an **original, strictly fictional** demonstration. Its synthetic units are not money, payroll, real company sales, or a client engagement.

## 02 · Data architecture

One order-grain fixture of **72 fictional records** covers four months, three regions and two channels. Each order has a date, region, channel, revenue, direct cost and assigned budget.

~~~mermaid
flowchart TD
  A[One committed fictional CSV fixture] --> B{Validate schema, decimals, dates, unique IDs}
  B -->|Reject| Z[Fail with evidence]
  B -->|Accept| C[Python Decimal aggregations]
  C --> D[Reconciled report.json]
  C --> E[Interactive offline HTML dashboard]
  A --> F[Matching SQL Server synthetic INSERTs]
  F --> G[Parameterized date-range query]
  G --> H[Original paginated .rdl definition]
  A --> I[Power BI DAX measure definitions]
  A --> J[Tableau calculated-field definitions]
  D --> K[Future independent native report reconciliation]
  H --> K
  I --> K
  J --> K
~~~

No real database credentials, customer records or AI provider keys are stored in this project.

## 03 · Metric contract

- **Revenue SU:** sum revenue across selected orders.
- **Margin SU:** sum revenue minus sum cost.
- **Margin %:** Margin SU / Revenue SU, calculated after applying the same filters to numerator and denominator.
- **Budget variance SU:** sum revenue minus sum budget. Positive is above the fictional target.
- **Orders:** count of unique order-grain records.

An average of order-level margin percentages would be mathematically incorrect for an aggregate margin KPI.

## 04 · Verified evidence

The [Python test suite](../engineering-labs/enterprise-bi-reporting/tests/test_report.py) verifies exactly 72 records, four monthly groupings, three regions, two channels, twelve month/region combinations and exact reconciliation of all aggregate sums.

It rejects duplicated order IDs, invalid dates/regions/channels, malformed monetary decimals, unexpected precision, and inconsistent source schemas. It independently inspects the SQL Server seed for exact equality with the committed CSV and checks the RDL XML structure, query parameters, data fields and absence of embedded passwords.

A CI run generates both **report.json** and a **standalone browser dashboard.html** as a downloadable workflow artifact.

## 05 · Current sample results

| Synthetic metric | Full fixture |
|---|---:|
| Order count | 72 |
| Revenue SU | 124,344.00 |
| Cost SU | 70,536.34 |
| Margin SU | 53,807.66 |
| Margin % | 43.27% |
| Budget SU | 123,444.00 |
| Budget variance SU | +900.00 |

These values were produced by the original offline code and dataset. **SU is not a real-world currency.**

## 06 · What we have not yet proved

| Platform | Current status |
|---|---|
| Python / HTML | Implemented, automated and output artifact generated |
| SQL Server | Schema, exact fixture and parameterized query committed; **this lab's SQL has not yet been executed against a live SQL Server** |
| Report Builder / SSRS | Original .rdl XML with dataset/parameters, statically validated; **no native rendering or PDF/XLSX export proof** |
| Power BI | Original DAX measures; **no native PBIX or DAX runtime result** |
| Tableau | Original calculated-field recipes; **no native TWB/TWBX runtime result** |
| Crystal Reports | Engineering methodology only; **no proprietary or native template** |

The independently tested SQL Performance Lab is not evidence that this new RDL report renders.

## 07 · Next verification gate

Run the schema, fixture and report on a disposable SQL Server instance; compare all twelve Month×Region rows with report.json. Then open the RDL in a licensed Report Builder environment, validate parameters and exports. Save native Power BI and Tableau files only after their calculations and filter behavior are tested.

[← All case studies](README.md) · [Data dictionary](../engineering-labs/enterprise-bi-reporting/docs/data-dictionary.md) · [Verification plan](../engineering-labs/enterprise-bi-reporting/docs/verification.md)

*Melissa Castro · Independent data engineering demonstration*

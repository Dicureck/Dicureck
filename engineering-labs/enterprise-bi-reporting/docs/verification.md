# Verification & Native Reporting Test Plan

## Fully offline, reproducible checks

From repository root, run:

~~~bash
python -m unittest discover -s engineering-labs/enterprise-bi-reporting/tests -v
python engineering-labs/enterprise-bi-reporting/src/report.py --out output/enterprise-bi
~~~

Outputs:
- report.json (exact financial-like totals and region/month/channel breakdown)
- dashboard.html (interactive offline UI with filters and bar visuals, no external scripts)

The tests cover valid fixtures, duplicate IDs, malformed dates, invalid two-decimal money, category rejection, zero denominators, source-to-SQL fixture parity, RDL XML parsing, query parameters and HTML script-safety.

## SQL Server reproduction (not yet run for this lab)

Create a new, empty, disposable test database named EnterpriseBILab on **localhost**, then execute schema.sql and seed.sql followed by report.sql with StartDate = 2026-01-01 and EndDate = 2026-05-01. The seed script refuses to insert when the target fact table already contains data.

**Never run these scripts on customer or shared production databases.** The standalone SQL Performance Lab has its own tested SQL Server integration; that does not prove this lab's RDL has been rendered.

## Platform-specific verification still required

- [ ] Open the RDL in Report Builder or SSRS with an isolated local database. Verify parameter prompts and query execution.
- [ ] Export RDL to PDF and Excel and compare all 12 Month×Region rows against report.json.
- [ ] Build and save an independent original Power BI PBIX using this exact fixture; validate DAX and slicer behavior.
- [ ] Build and save an original Tableau workbook using this exact fixture; validate filter context, export and percentages.
- [ ] Only package a Crystal Reports template after a licensed tool/runtime is available and tested.
- [ ] Add synthetic screenshots of actual native runtimes and their version numbers.

**Security:** no usernames, passwords, real client data, proprietary logic, external APIs or destination email addresses in these artifacts.

[Lab README](../README.md) · [Technical case study](../../../case-studies/enterprise-bi-reporting.md)

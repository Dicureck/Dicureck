# Paginated Report & BI Interoperability Design

**Concept:** monthly fictional operating summary grouped by business unit.

**Inputs:** date window, unit filter, exported synthetic data. **Measures:** total revenue, total cost, operating margin. Declare aggregation at the order grain and reconcile to the CLI's JSON output.

**Report Builder / SSRS:** design a parameterized RDL using a read-only synthetic SQL data source. Include repeatable page header, print-safe table widths, subtotal and grand total, null-state message, and CSV/PDF parity testing. An RDL binary/native report is **not included** here.

**Crystal Reports:** group by business unit, verify formula evaluation order, suppress empty groups deliberately, and validate page breaks and exports. No licensed project binary is included.

**Tableau / Power BI:** model dimensions at declared grain and compare aggregate measures to the JSON output before publishing visualizations. Native .twb/.pbix files are not included.

**Evidence gate:** do not label these product integrations tested until opened, executed and reconciled in their respective runtimes.

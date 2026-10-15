# Data Dictionary · Synthetic Enterprise BI

**Classification: fabricated demonstration data only.** Financial amounts are in synthetic units **SU**, not GTQ or USD.

## Record grain and categories

The source is **one unique sale order per row**, not order lines. Exactly **72 orders** = four months × three regions × two channels × three example orders. No personal records or real-world customers.

| Column | Type | Valid values and intended meaning |
|---|---|---|
| order_id | varchar(5) | S0001 through S0072, unique business key |
| sale_date | ISO date | January–April 2026, exact YYYY-MM-DD |
| region | category | North, Central, South |
| channel | category | Digital, Partner |
| revenue_su | decimal(19,2) | Nonnegative revenue-like synthetic units |
| cost_su | decimal(19,2) | Nonnegative direct costs, no larger than revenue in this fixture |
| budget_su | decimal(19,2) | Synthetic revenue target defined at order grain |

A future star schema could separate DimDate, DimRegion and DimChannel with one-to-many links to FactSyntheticSales. The published demo intentionally keeps a single fact table to avoid introducing unvalidated joins.

## Metric contracts

- **Orders:** COUNTROWS at exact order grain, or COUNTD(order_id).
- **Revenue SU:** sum revenue_su.
- **Cost SU:** sum cost_su.
- **Budget SU:** sum budget_su.
- **Margin SU:** sum revenue_su minus sum cost_su.
- **Margin %:** Margin SU / Revenue SU; NULL for zero revenue.
- **Budget Variance SU:** sum revenue_su minus sum budget_su; positive means above the synthetic target.
- **Budget Variance %:** Budget Variance SU / Budget SU; NULL for zero budget.

**Never average ratios calculated per order.** For Region, Channel, Month and Month+Region breakdowns, verify exact aggregate sums and order counts reconcile against the unfiltered report.

## Date parameters

The RDL / SQL query uses a **half-open** date window: StartDate inclusive, EndDate exclusive. Default: January 1, 2026 → May 1, 2026. Filtering the Python report to a comparable period is necessary before comparing alternative date windows.

[Original fixture](../fixtures/sales.csv) · [Python validation](../src/report.py) · [RDL template](../rdl/Enterprise-Sales-Summary.rdl)

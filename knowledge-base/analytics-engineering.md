# Analytics Engineering & BI Design

**Focus:** KPIs · semantic models · dimensional design · business decisions

Good dashboards start with questions, metric definitions and data grain—not colors or charts.

## 01 · Build the decision model

1. **Decision:** who acts on the indicator, and what will they change?
2. **Grain:** exactly what does one input record represent?
3. **Dimensions:** date, territory, channel, product or priority.
4. **Measures:** numerator, denominator, exclusions, and currency/time policy.
5. **Model:** separate fact tables from reusable dimensions when appropriate.
6. **Validation:** reconcile aggregations to source and independent fixtures.
7. **Delivery:** provide accessible filters, labels and interpretation notes.

## 02 · Three fictional case studies

| Domain | Grain | Example decision metric | Risk to call out |
|---|---|---|---|
| Logistics | Delivery attempt | On-time attempts / all attempts | Excluding failed delivery attempts can bias SLA |
| Finance | Ledger posting | Revenue minus direct cost | Sign conventions and currency conversion |
| Incidents | One incident | Resolved within SLA / resolved | Open overdue incidents must be reported separately |

These are *demonstration* definitions. A real organization's metric contracts may differ.

## 03 · Power BI patterns

- Build a star schema with declared relationships and direction of filtering.
- Mark a complete Date table for time intelligence.
- Prefer measures for context-dependent calculations.
- Document DAX numerator/denominator semantics and blank-value behavior.
- Test row-level security and accessibility independently if used.

Example **conceptual** DAX on fictional model fields:
~~~dax
Total Revenue = SUM ( FactSales[RevenueAmount] )
Total Orders = DISTINCTCOUNT ( FactSales[OrderID] )
Average Order Value = DIVIDE ( [Total Revenue], [Total Orders] )
~~~

This assumes the modeled data grain and relationships are correct; those measures are not verified against a particular .pbix here.

## 04 · Visual quality gate

- Show time window, update cadence, unit and source of each KPI.
- Use consistent colors and accessible contrast.
- Avoid ranking raw rates for tiny cohorts without count/context.
- Include an explicit empty/error state.
- Test both desktop and mobile layout.
- Make synthetic demo provenance immediately visible.

**Companion labs:** [Logistics](https://github.com/Dicureck/logistics-route-intelligence) · [Financial](https://github.com/Dicureck/financial-intelligence-lab) · [Incidents](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales)

[Reporting platforms guide](reporting-platforms.md)

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*

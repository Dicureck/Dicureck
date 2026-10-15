# BI Calculation Examples | Power BI DAX & Tableau

**Methodology and original illustrative calculations only.** These snippets assume a fictional order-grain fact model. No working .pbix or Tableau workbook is claimed here.

## Power BI · fictional FactOrders model

Assumed fields: FactOrders[OrderID], FactOrders[RevenueSU], FactOrders[CostSU] and Date[Date], with validated model grain and relationships.

~~~dax
Revenue SU = SUM ( FactOrders[RevenueSU] )
Cost SU = SUM ( FactOrders[CostSU] )
Operating Profit SU = [Revenue SU] - [Cost SU]
Operating Margin % = DIVIDE ( [Operating Profit SU], [Revenue SU] )
Orders = DISTINCTCOUNT ( FactOrders[OrderID] )
~~~

Checks: [Operating Profit SU] equals total revenue minus total cost at all filter grains; zero-revenue contexts return BLANK instead of division error; dates cover all facts. These snippets are not validated against a published Power BI model.

## Tableau · fictional orders

**Calculated fields** (adapt to your dataset's actual field names and types):

~~~text
// Revenue SU
SUM([Revenue SU])

// Operating Profit SU
SUM([Revenue SU]) - SUM([Cost SU])

// Operating Margin %
IF SUM([Revenue SU]) = 0 THEN NULL
ELSE (SUM([Revenue SU]) - SUM([Cost SU])) / SUM([Revenue SU])
END

// Order Count (when ID granularity is one row per order)
COUNTD([Order ID])
~~~

Important: Tableau's order of operations, FIXED LOD calculations and context filters can change what a measure means. Explicitly test the numerator and denominator under filter changes.

## Comparability rules

1. Declare fact grain, required filters and NULL handling first.
2. Avoid summing row-level margins or averaging rates across unequal groups.
3. Validate output against the same synthetic fixture rows, not unrelated demos.
4. Publish native visual assets and runtime results before claiming a tool-specific implementation.

[Reporting platforms](reporting-platforms.md) · [Analytics engineering](analytics-engineering.md) · [Portfolio](https://dicureck.github.io/)

# Tableau | Synthetic Sales Calculations

**Input:** import the [same 72-row fictional CSV](../fixtures/sales.csv). One row per order. Set sale_date to Date and amounts to decimal Number. These are manually enterable formulas, **not** a tested TWB/TWBX workbook.

## Calculated fields

**Orders**
~~~text
COUNTD([order_id])
~~~

**Revenue SU**
~~~text
SUM([revenue_su])
~~~

**Cost SU**
~~~text
SUM([cost_su])
~~~

**Budget SU**
~~~text
SUM([budget_su])
~~~

**Margin SU**
~~~text
SUM([revenue_su]) - SUM([cost_su])
~~~

**Margin %**
~~~text
IF SUM([revenue_su]) = 0 THEN NULL
ELSE (SUM([revenue_su]) - SUM([cost_su])) / SUM([revenue_su])
END
~~~

**Budget Variance SU**
~~~text
SUM([revenue_su]) - SUM([budget_su])
~~~

**Budget Variance %**
~~~text
IF SUM([budget_su]) = 0 THEN NULL
ELSE (SUM([revenue_su]) - SUM([budget_su])) / SUM([budget_su])
END
~~~

**Month**
~~~text
DATETRUNC('month', [sale_date])
~~~

## Chart suggestions and boundaries

Use monthly Revenue as bars; Region as filter; Orders, Revenue, Margin % and Budget Variance as KPI cards. A filter applied only to the numerator invalidates ratios. Reconcile all outputs against the Python-generated report.json from **the same source rows**.

Tableau model, workbook, filters and export behavior have **not been verified in a Tableau runtime**.

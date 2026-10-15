# Case Study 02 · Financial Intelligence

**Context:** independent, fictional monthly finance dashboard.

## Problem

A reporting team needs transparent explanations of revenue, direct costs, operating expenses, profit and differences from budget. Summing row-level percentages can cause misleading conclusions.

## Data contract

The front-end browser demo generates 36 synthetic rows: 3 channels × 12 months. Each row has revenue, costs, operating expenses, budgeted revenue and derived operating profit.

| Metric | Definition | Constraint |
|---|---|---|
| Revenue | Sum of revenue | Synthetic units only, not a real currency |
| Operating profit | Sum(revenue − costs − expenses) | Reconciles to source rows |
| Operating margin | 100 × total profit / total revenue | Recompute after filtering, never average row margins |
| Budget variance | 100 × (total revenue − total budget revenue) / total budget revenue | Explicit target denominator |

## Architecture

~~~mermaid
flowchart LR
  A["Synthetic fictional ledger rows"] --> B["Channel filter"]
  B --> C["Additive aggregate measures"]
  C --> D["Operating margin and variance"]
  C --> E["Monthly revenue chart"]
  B --> F["Filtered CSV download"]
~~~

## Decisions and tests

- Compute profit explicitly from the synthetic financial rows.
- Aggregate monetary-like measures before dividing for margin or variance.
- Label output as **SU — synthetic units**, not GTQ/USD or live financial data.
- Browser smoke tests verify that channel changes alter the metric panel without JavaScript errors.

## Limitations

No general-ledger integration, certified reporting model or accounting system has been tested. The portfolio demo is distinct from the [Financial Intelligence Lab](https://github.com/Dicureck/financial-intelligence-lab); outputs are not claimed to match unless reconciliation tests are performed.

**[Open interactive financial dashboard →](https://dicureck.github.io/?demo=finance#lab)**  
[Source laboratory](https://github.com/Dicureck/financial-intelligence-lab) · [BI methodology](../knowledge-base/analytics-engineering.md)

# Case Study 01 · Logistics & Route Intelligence

**Context:** independent synthetic delivery-operations lab.

## Problem

An operations analyst needs to understand how fulfillment changes across regions without conflating completed deliveries, on-time attempts and planned distance. Naive SLA definitions can make a low-performing operation look successful by excluding missed attempts.

## Data contract

The browser demo locally generates 1,056 fictional delivery attempts: 4 regions × 12 months × 22 attempts per region/month, using a fixed pseudo-random seed. Each record has month, region, successful, onTime, plannedKm and actualKm. The source of truth for this demo's KPI implementation is [app.js](https://github.com/Dicureck/dicureck.github.io/blob/main/app.js).

| Metric | Definition | Validation |
|---|---|---|
| Attempts | Number of generated records in filter | Count raw records |
| On-time rate | 100 × onTime attempts / **all** attempts | onTime implies successful |
| Successful | Count of attempts marked successful | Count within filter |
| Distance variance | 100 × (sum actualKm − sum plannedKm) / sum plannedKm | Both sums taken at same grain |

## Architecture

~~~mermaid
flowchart LR
  A["Deterministic synthetic attempts"] --> B["Region filter"]
  B --> C["Metric calculations"]
  C --> D["Monthly SVG chart"]
  C --> E["CSV export"]
  C --> F["Metric definitions"]
~~~

## Engineering decisions

- The region filter recomputes all values from the same records.
- SVG charts use the same filtered series as the KPI cards.
- CSV exports are the filtered fictional rows, not private extracts.
- The UI describes distances as illustrative; it does **not** claim road-routing optimization or real geocoding.

## Verification

Automated front-end tests check the selected dashboard, metric updates, project filters and browser errors. These are **synthetic UI checks**, not evidence of a dispatch engine's operational accuracy.

## Further work

Link source lab's native BI implementation and compare calculations against independently generated fixture expectations, after reconciliation. Add scenario comparisons with explicit denominator control.

**[Open interactive logistics dashboard →](https://dicureck.github.io/?demo=logistics#lab)**  
[Source laboratory](https://github.com/Dicureck/logistics-route-intelligence) · [Knowledge Base](../knowledge-base/analytics-engineering.md)

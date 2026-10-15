# Case Study 03 · Operational Incident Intelligence

**Context:** independent synthetic service-ticket intelligence.

## Problem

An incident dashboard can conceal service risk when it reports SLA compliance among resolved tickets but omits open overdue incidents. The goal is to keep outcome rates and backlog metrics separate.

## Data contract

The front-end demo generates 384 fictional incidents: 12 months × 32 records. Each has month, category, severity, resolved, durationHours, ageHours, withinSla and overdueOpen.

Demonstration time limits: Critical 8h, High 24h, Medium 48h, Low 96h. These values are **fictional design assumptions**, not client SLAs.

| Metric | Definition | Trade-off |
|---|---|---|
| Total incidents | All records in filter | Includes open + resolved |
| Resolved within SLA | 100 × resolved AND withinSla / **all resolved** | Excludes unresolved from rate |
| Open backlog | All records not resolved | Must be visible beside resolved SLA |
| Overdue open | Unresolved records exceeding severity threshold | Exposes risk hidden by resolved-only rate |

## Architecture

~~~mermaid
flowchart LR
  A["Synthetic incidents"] --> B["Category filter"]
  B --> C["Resolved incidents"]
  B --> D["Open incidents"]
  C --> E["SLA denominator and monthly trend"]
  D --> F["Overdue backlog"]
  B --> G["Filtered CSV download"]
~~~

## Validation and limitations

UI tests cover switching to Incident mode, filtering and rendering updated metrics. No live ticketing integration, dynamic triage model, alerting service or production SLA certification is implied.

Further work: test the agreement of severity-based thresholds against independent fixture files; document how reopened tickets and paused timers are represented before applying this method to real service-management data.

**[Open interactive incident dashboard →](https://dicureck.github.io/?demo=incidents#lab)**  
[Source laboratory](https://github.com/Dicureck/Dashboard-an-lisis-de-incidencias-operacionales) · [Analytics engineering](../knowledge-base/analytics-engineering.md)

# Analytics Engineering | Explainable KPI Design

A good dashboard starts with a decision, not a chart.

~~~mermaid
flowchart TD
 A[Business question] --> B[Define the metric and denominator]
 B --> C[State input grain and exclusions]
 C --> D[Model facts and dimensions]
 D --> E[Reconcile independent totals]
 E --> F[Create accessible dashboards]
 F --> G[Explain limits and uncertainty]
~~~

## Fictional examples

| Domain | Important metric boundary |
|---|---|
| [Delivery operations](https://dicureck.github.io/?demo=logistics#lab) | Count all attempts when calculating on-time rate |
| [Financial intelligence](https://dicureck.github.io/?demo=finance#lab) | Define signs, periods, units and budget conventions |
| [Incident analytics](https://dicureck.github.io/?demo=incidents#lab) | Separate resolved SLA from open overdue backlog |

The web dashboards run in the browser with invented records, not live company data. Metrics are examples, not corporate performance statements.

[Analytics Engineering guide](https://github.com/Dicureck/Dicureck/blob/main/knowledge-base/analytics-engineering.md).


---

All records and examples are original and fictional. [Engineering portfolio](https://dicureck.github.io/) · [Public Projects Board](https://github.com/users/Dicureck/projects/1/views/2).

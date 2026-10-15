# Data Quality & Duplicate-Aware Reconciliation

**Schema contracts · row identities · NULL handling · reproducible checks**

Equal row counts and equal set values are not sufficient when duplicates matter.

## Quality validation

~~~mermaid
flowchart TD
 A[Original fictional data] --> B{Expected schema?}
 B -->|No| X[Reject and record evidence]
 B -->|Yes| C{Valid keys and business rules?}
 C -->|No| X
 C -->|Yes| D[Normalize under declared contract]
 D --> E[Compare complete row multiplicities]
 E -->|Different| X
 E -->|Equal| F[Publish bounded result]
~~~

## Minimal Python example

~~~python
from collections import Counter

before = [("A", 10), ("A", 10), ("B", 20)]
after = [("A", 10), ("B", 20), ("B", 20)]

assert Counter(before) != Counter(after)
assert Counter(before) - Counter(after) == Counter({("A", 10): 1})
~~~

Check required fields, units and scale, null conventions, date and timezone boundaries, unexpected records and repeatability. Never publish real customer records.

[Data Quality Toolkit](https://github.com/Dicureck/data-quality-toolkit) · [Detailed guide](https://github.com/Dicureck/Dicureck/blob/main/knowledge-base/data-quality.md).


---

All records and examples are original and fictional. [Engineering portfolio](https://dicureck.github.io/) · [Public Projects Board](https://github.com/users/Dicureck/projects/1/views/2).

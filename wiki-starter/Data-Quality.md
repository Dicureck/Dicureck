# Data Quality | Native Wiki Page Draft

> **Source-controlled draft only**, not an automatically created native Wiki page. Canonical guide: [Data Quality Engineering](../knowledge-base/data-quality.md).

## A repeatable verification process

~~~mermaid
flowchart TD
  A[Original synthetic input] --> B{Schema and required fields}
  B -->|Invalid| X[Reject with clear evidence]
  B -->|Valid| C[Keys, completeness and semantics]
  C -->|Invalid| X
  C -->|Valid| D[Normalize under declared contract]
  D --> E[Compare full-row multiplicity]
  E -->|Difference| X
  E -->|Equivalent| F[Publish bounded validation result]
~~~

Count every unique complete row and compare its multiplicity. Row-count equality and set equality alone do not establish equivalence.

## Checklist

- [ ] Schema and grain documented
- [ ] NULL, timezone, decimals and string semantics defined
- [ ] Duplicate/missing records detected
- [ ] Negative fixtures and failed results retained
- [ ] No real personal/customer records or secrets committed

**Companion:** [Data Quality Toolkit](https://github.com/Dicureck/data-quality-toolkit).

[Knowledge Base](../knowledge-base/README.md) · [Portfolio](https://dicureck.github.io/)

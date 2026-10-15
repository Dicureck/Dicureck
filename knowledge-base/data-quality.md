# Data Quality & Validation Patterns

A data product is credible when another engineer can independently reproduce its output and verify the business assumptions.

## Five useful layers

| Layer | Example question | Typical check |
| --- | --- | --- |
| Schema | Did the shape change? | Required columns, types, keys |
| Completeness | Is anything missing? | Null coverage, expected date range |
| Integrity | Are relationships consistent? | Unique IDs and foreign-key checks |
| Semantics | Does the calculation still mean the same? | Rule-level fixtures and boundary cases |
| Reconciliation | Do two implementations return the same records? | Complete-row multiset comparison |

## Duplicate-aware reconciliation

Ordinary set equality can silently ignore multiplicity. A safer comparison counts each canonical row and diffs those counters. When using CSV, preserve column order and specify explicit rules for `NULL`, date formatting, decimals, and encoding before comparing.

## Release gates

- Declare the source of truth and data provenance.
- Use generated test data without personal identifiers.
- Keep inputs, assertions, and expected outputs version controlled.
- Publish limitations and explain every excluded condition.
- Avoid actual credentials, employee data, client identifiers, and production endpoints.

**See also:** [SQL performance](sql-performance.md) · [Database migration](database-migration.md)

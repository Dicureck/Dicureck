# Data Quality Engineering

**Focus:** data contracts · schema drift · validation · duplicate-aware reconciliation

A data pipeline is trustworthy when another engineer can verify both its assumptions and its output.

## 01 · Quality gates

| Gate | Example | Failure behavior |
|---|---|---|
| Schema | Required columns and types | Reject unknown/broken schema |
| Completeness | Mandatory IDs and timestamps | Reject missing critical fields |
| Uniqueness | One row per declared key | Report duplicate keys |
| Referential integrity | Orders refer to valid customers | Report orphan records |
| Business semantics | Nonnegative units, valid event status | Flag invalid records |
| Reconciliation | Old and new complete outputs agree | Fail on missing/extra duplicates |

## 02 · Duplicate-aware Python example

These are fictional records, represented as tuples with explicit column order.

~~~python
from collections import Counter

before = [
    ("A100", "2026-01-01", "19.90"),
    ("A100", "2026-01-01", "19.90"),
    ("A200", "2026-01-02", "15.00"),
]
after = [
    ("A100", "2026-01-01", "19.90"),
    ("A200", "2026-01-02", "15.00"),
    ("A200", "2026-01-02", "15.00"),
]

missing = Counter(before) - Counter(after)
unexpected = Counter(after) - Counter(before)

assert missing[("A100", "2026-01-01", "19.90")] == 1
assert unexpected[("A200", "2026-01-02", "15.00")] == 1
~~~

Both inputs contain three rows, but they are **not equivalent**. Sets and aggregated totals could overlook this.

## 03 · Canonicalization contract

Before comparing exports, specify:
- key and column order;
- NULL versus empty string representation;
- date/time formats and time zone;
- decimal precision and rounding;
- character normalization and whitespace policy;
- case sensitivity and relevant collation rules.

Do not trim, round or lowercase silently: doing so can hide real defects.

## 04 · CI and release evidence

Use tiny positive/negative fixtures, deterministic generators and exit codes that fail closed. Save validation summaries as inspectable JSON. Mask or omit sensitive values from logs. CI can prove that specific tests passed; it does not certify a deployment for production.

**Companion:** [Data Quality Toolkit](https://github.com/Dicureck/data-quality-toolkit). See also [Python and pandas](python-pandas.md) and [SQL Performance](sql-performance.md).

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*

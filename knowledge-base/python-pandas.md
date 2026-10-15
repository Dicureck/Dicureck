# Python & pandas | Reproducible Data Pipelines

**Focus:** predictable transformations · typed inputs · reusable functions · tests

Python and pandas are valuable when a workflow makes its assumptions visible and produces stable outputs from known inputs.

## 01 · Design steps

1. Define the input schema and expected grain.
2. Validate required columns, duplicate keys and allowed values.
3. Use explicit date/numeric conversions and report failures.
4. Keep transformations pure when possible.
5. Use deterministic sorting before saving final outputs.
6. Assert business identities and compare totals at multiple grains.
7. Version code and fixtures, not private datasets.

## 02 · Example: fictional sales

~~~python
import pandas as pd

sales = pd.DataFrame({
    "order_id": ["O1", "O2", "O3"],
    "region": ["North", "South", "North"],
    "amount": ["12.50", "30.00", "7.50"],
})

required = {"order_id", "region", "amount"}
assert required.issubset(sales.columns)
assert sales["order_id"].notna().all()
assert sales["order_id"].is_unique

sales["amount"] = pd.to_numeric(sales["amount"], errors="raise")
assert sales["amount"].notna().all()

by_region = (
    sales.groupby("region", as_index=False, dropna=False)["amount"]
         .sum()
         .sort_values("region", kind="stable")
)
assert abs(by_region["amount"].sum() - 50.0) < 1e-9
print(by_region.to_string(index=False))
~~~

For financial calculations, prefer a documented fixed-precision/Decimal approach where binary floating-point rounding could change results. The example uses tiny fabricated values only.

## 03 · Testing beyond happy paths

- Empty files and missing required columns
- Unexpected and null regions
- Duplicate IDs and duplicate entire rows
- Bad date formats and negative values
- Timezone boundaries and year-end reports
- Unsorted input rows
- Output idempotency across repeated runs

## 04 · Engineering layout

~~~text
project/
  src/package/
  tests/
  examples/synthetic.csv
  docs/
  pyproject.toml
  README.md
~~~

A good README explains setup, CLI behavior, input/output contracts, deterministic seeds, and limitations.

**Live examples:** [Logistics & Route Intelligence](https://github.com/Dicureck/logistics-route-intelligence) · [Financial Intelligence Lab](https://github.com/Dicureck/financial-intelligence-lab) · [Data Quality Toolkit](https://github.com/Dicureck/data-quality-toolkit)

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*

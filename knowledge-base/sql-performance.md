# SQL Performance Engineering

**Focus:** T-SQL · SARGability · execution plans · correctness gates · repeatable measurements

> Faster is useful only when the query still returns the right answer.

## 01 · An optimization workflow

1. Define the expected result: keys, columns, filters, NULL handling, tie-breaking and duplicate policy.
2. Capture a baseline: input size, statistics, engine version, parameters, logical reads, CPU, elapsed time and execution plan.
3. Identify one suspected cause of cost. Be wary of non-SARGable filters, row amplification and correlated repeated work.
4. Apply an isolated change with a rollback plan.
5. Compare complete results, including duplicate-row multiplicity.
6. Repeat measurements under recorded conditions; report distributions instead of selecting one favorable run.
7. Document what you tested and what remains unverified.

## 02 · Synthetic SQL Server example

Assume a fictional **dbo.sample_orders** table with a datetime2 order_date.

Baseline:
~~~sql
DECLARE @date date = '2026-02-01';

SELECT order_id, customer_id, order_date
FROM dbo.sample_orders
WHERE CONVERT(date, order_date) = @date;
~~~

Candidate:
~~~sql
DECLARE @date date = '2026-02-01';

SELECT order_id, customer_id, order_date
FROM dbo.sample_orders
WHERE order_date >= @date
  AND order_date < DATEADD(day, 1, @date);
~~~

The second predicate is a straightforward half-open range and is typically easier to seek with a suitable index. SQL Server can optimize some CONVERT(date) patterns too; **do not claim speedup without the actual plan and measurements**.

## 03 · Collect comparable evidence

~~~sql
SET STATISTICS IO ON;
SET STATISTICS TIME ON;

-- Run the baseline and candidate with comparable parameters.

SET STATISTICS IO OFF;
SET STATISTICS TIME OFF;
~~~

Capture actual execution plans where possible. Track logical reads, CPU, elapsed time, spills, memory grants and cardinality estimates. Note warm/cold cache, parameter sensitivity, concurrency and index changes. Never clear a shared server's cache just to improve a portfolio measurement.

## 04 · Exactness before benchmarking

Equal row counts and equal SUM values are insufficient. A valid comparison must catch:
- missing rows and unexpected rows;
- duplicated records with the wrong frequency;
- altered NULL or numeric precision;
- boundary-date differences;
- order only where part of the contract.

For SQL exports, normalize schema, data types and formatting with a documented policy, then compare complete-row counters. Hash totals alone are not proof of equivalence.

## 05 · Publishing results responsibly

A defensible benchmark includes environment/version, data volume, parameters, indexes, scripts, independent verification, all individual timings and summarized statistics such as median and p95. Differences between runs can come from cache or concurrency, not only the query change.

**Companion lab:** [SQL Performance Lab](https://github.com/Dicureck/sql-performance-lab). A real SQL Server Developer container [completed an integration and measured CI smoke run](https://github.com/Dicureck/sql-performance-lab/blob/main/docs/verified-ci-benchmark-2026-10-15.md) on **2,000 synthetic customers, 12,000 orders and 36,000 order lines**. The date predicate example measured **3.136 ms** baseline vs **1.928 ms** candidate median in three measurements, with full-row validation; the aggregate example measured 17.929 vs 16.117 ms. These are observations from **one CI execution**, not production benchmarks or guaranteed improvements. SQL Server execution plans and logical reads remain a separate step.

## Review checklist

- [ ] Query contract explicit
- [ ] Indexes and statistics documented
- [ ] Baseline and candidate plans captured
- [ ] Complete row multisets equal
- [ ] Warmup and timing policies disclosed
- [ ] Raw timing records reproducible
- [ ] Rollback and limitations recorded

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*

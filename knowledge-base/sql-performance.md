# SQL Performance Engineering

*Companion project: [SQL Performance Lab](https://github.com/Dicureck/sql-performance-lab).*

## A reliable optimization loop

1. State the intended result as a testable contract (keys, filters, null behavior, data types, ordering, and duplicate policy).
2. Create synthetic datasets of realistic *shape*, including skew, sparse values, and edge cases.
3. Capture a baseline **before** adding hints or indexes. Document engine version, cardinality, parameters, and query plan.
4. Identify cost drivers: excessive scans, non-sargable predicates, row multiplication, poor estimates, sorts, and repeated computation.
5. Change one hypothesis at a time, keeping a rollback path.
6. Compare old and new outputs by a **multiset** of complete rows — totals and simple set equality can miss duplicated or missing records.
7. Measure repeated runs and report median, spread, workload, cache effects, and hardware conditions.

## Things not to claim

- Faster execution from a static code review alone.
- A universal percentage improvement from a single measurement.
- Semantic equivalence from matching row counts or aggregated totals.
- Production readiness based only on synthetic data.

## Checklist

- [ ] Functional contracts written down
- [ ] Baseline and candidate executed under comparable conditions
- [ ] Full-result and multiplicity checks pass
- [ ] Query plans compared
- [ ] Repeated measurements captured
- [ ] Limitations and rollback documented

No proprietary stored procedures or client results are included here.

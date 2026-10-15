# Database Migration Engineering

*Companion project: [Oracle Migration Toolkit](https://github.com/Dicureck/oracle-migration-toolkit).*

## Migration is semantic, not only syntactic

A trustworthy SQL Server → Oracle transition requires more than replacing `ISNULL`, `GETDATE`, `TOP`, or `IDENTITY` mechanically. Define the data contract and deployment boundaries first.

### Assessment

- Inventory objects and cross-schema dependencies, including dynamic SQL and stored expressions.
- Identify type differences (`datetime`, `NUMBER`, `DECIMAL`, `NVARCHAR`, `CLOB`, `XMLTYPE`, binary IDs).
- Record transaction behavior, locking, session state, time-zone assumptions, and NLS-dependent expressions.
- Detect unsupported constructs and mark uncertainty. Do not promise automatic conversion of arbitrary business logic.

### Transformation

- Separate DDL and schema prerequisites from seed configuration and operational DML.
- Validate deterministic ordering, date boundaries, `NULL` semantics, and identity generation.
- Translate procedures and functions by signature; use the target database dictionary to verify every dependency.
- Preserve a reversible deployment plan, tested backups, and object-level audit trail.

### Validation gates

1. Static transformation checks (offline).
2. Successful compilation on the target engine.
3. Controlled functional tests for edge cases and row multiplicity.
4. Cross-engine reconciliation and performance testing.
5. Explicit sign-off before production deployment.

The public toolkit demonstrates early gates; engine-to-engine equivalence is **not** assumed from offline tests.

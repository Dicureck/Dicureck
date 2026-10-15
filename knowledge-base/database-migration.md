# SQL Server → Oracle | Database Migration Engineering

**Focus:** T-SQL · PL/SQL · Oracle 12c+ · schema dependencies · validation

> A migration succeeds when behavior is preserved, not merely when syntax compiles.

## 01 · Assessment before translation

Build an inventory of tables, views, functions, procedures, sequences, jobs, and cross-schema references. Record object ownership, signatures, execution order, and the code's required database versions. Review dynamic SQL, stored formulas, XML/JSON handling, transactions, exception behavior, collations, and session-dependent expressions.

Treat every uncertainty as an explicit validation item, rather than guessing a target implementation.

## 02 · Compatibility matrix

| SQL Server concept | Oracle candidate | Verification needed |
|---|---|---|
| INT, BIGINT | NUMBER(10), NUMBER(19) | Exact ranges and application bindings |
| DECIMAL(p,s) | NUMBER(p,s) | Precision, scale, rounding |
| VARCHAR / NVARCHAR | VARCHAR2 / NVARCHAR2 | Byte vs character length, Unicode |
| DATETIME / DATETIME2 | DATE / TIMESTAMP | Precision, timezone assumptions |
| BIT | NUMBER(1) with constraint | Valid values, NULL semantics |
| UNIQUEIDENTIFIER | RAW(16) or VARCHAR2(36) | Serialization and joins |
| XML | XMLTYPE or CLOB | Actual querying and storage patterns |
| IDENTITY | Identity or sequence | Generation, gaps, concurrency |
| TOP(n) | FETCH FIRST n ROWS ONLY | Explicit ordering and tie behavior |

Mappings are *candidates*, not universal equivalents. Oracle version and compatibility settings matter.

## 03 · Paired, original examples

**Deterministic top-five selection.** Add a unique tie-breaker in both engines.

SQL Server:
~~~sql
SELECT TOP (5) employee_id, salary
FROM dbo.sample_employees
ORDER BY salary DESC, employee_id;
~~~

Oracle 12c+:
~~~sql
SELECT employee_id, salary
FROM sample_employees
ORDER BY salary DESC, employee_id
FETCH FIRST 5 ROWS ONLY;
~~~

**A count returned from a procedure.** SQL Server can emit a result set; an Oracle OUT parameter is one explicit alternative, not a drop-in equivalent.

SQL Server:
~~~sql
CREATE OR ALTER PROCEDURE dbo.sample_employee_count
AS
BEGIN
  SET NOCOUNT ON;
  SELECT COUNT(*) AS total_employees
  FROM dbo.sample_employees;
END;
~~~

Oracle:
~~~sql
CREATE OR REPLACE PROCEDURE sample_employee_count (
  p_total OUT NUMBER
) AS
BEGIN
  SELECT COUNT(*)
    INTO p_total
    FROM sample_employees;
END;
/
~~~

Calling applications must be adapted to the chosen Oracle interface.

## 04 · Semantic traps

- **DATEDIFF** counts date-part boundaries in SQL Server; Oracle DATE subtraction returns elapsed days. A literal text replacement may change business results.
- **GETDATE vs SYSDATE:** both are often used for server-local time, but precision, clock and timezone contexts must be verified. Consider SYSTIMESTAMP where needed.
- **ISNULL vs NVL:** pay attention to inferred data type and conversion; COALESCE is not automatically behaviorally identical either.
- **Empty strings:** Oracle usually treats zero-length character strings as NULL.
- **Transactions:** Oracle DDL commonly causes implicit commits; plan DDL rollout and recovery independently of DML rollback.
- **Identifiers:** limits and case sensitivity depend on version/compatibility and quoted naming conventions.
- **Sequences:** do not use MAX(id)+1 as a concurrency-safe sequence replacement.

## 05 · Dependency-aware installation

1. Validate privileges, schema names, types, and version.
2. Install prerequisite tables, sequences, and SQL types.
3. Install functions/procedures in dependency order; detect missing references and cycles.
4. Compile and inspect errors before enabling dependent views or formulas.
5. Load synthetic configuration only after referential integrity is established.
6. Execute authorized functional tests and post-deployment checks.
7. Preserve a verified recovery procedure and audit trail.

There is no single universal object order; the graph determines the sequence.

## 06 · Validation gates

| Gate | Evidence | Does not prove |
|---|---|---|
| Static assessment | Risks and object inventory | Successful compilation |
| Target compilation | Object status and signatures | Equivalent business behavior |
| Functional fixtures | Boundary cases and rules | Complete cross-engine parity |
| Reconciliation | Full-row multiplicity and numeric conventions | Performance similarity |
| Performance checks | Repeated measurements on each engine | Universal speedup |
| Release approval | Sign-off, recovery rehearsal | No future defects |

The public [Oracle Migration Toolkit](https://github.com/Dicureck/oracle-migration-toolkit) demonstrates conservative *offline* checks, dependency planning and synthetic reconciliation. It does not claim live SQL Server-to-Oracle equivalence.

## 07 · Engineering review checklist

- [ ] Identified object ownership and current signatures
- [ ] Documented SQL Server semantics and Oracle alternatives
- [ ] Defined NULL/date/precision/collation acceptance criteria
- [ ] Ordered objects by real dependencies
- [ ] Compiled against the selected Oracle version
- [ ] Compared duplicates, missing records and edge cases
- [ ] Recorded deployment and rollback decisions
- [ ] Obtained functional approval before release

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*

# SQL Server → Oracle | Database Migration

**T-SQL · PL/SQL · data types · dependencies · business-rule verification**

Migrate **behavior**, not syntax alone. A procedure that compiles can still produce a different result.

## Migration workflow

~~~mermaid
flowchart TD
 A[Inventory source objects] --> B[Map signatures and dependencies]
 B --> C[Assess date, NULL and precision semantics]
 C --> D[Compile target Oracle examples]
 D --> E[Run synthetic boundary tests]
 E --> F[Reconcile complete source/target results]
 F --> G{Business rules verified?}
 G -->|No| C
 G -->|Yes| H[Controlled release and rollback plan]
~~~

## Compatibility checkpoints

| Topic | Typical migration concern |
|---|---|
| SQL Server DATEDIFF vs Oracle DATE subtraction | Date boundaries vs elapsed days |
| Empty string and NULL | Oracle character handling differs |
| VARCHAR, NVARCHAR, number precision | Encoding, length and rounding |
| Identity and sequences | Concurrency and key-generation policy |
| Procedures and functions | Parameters, exceptions and transaction boundaries |

The [Oracle Migration Toolkit](https://github.com/Dicureck/oracle-migration-toolkit) now has **[verified real SQL Server 2022 ↔ Oracle Free 26ai functional parity](https://github.com/Dicureck/oracle-migration-toolkit/blob/main/docs/verified-cross-engine-parity-2026-10-16.md)** for **260 original fictional orders**, February summaries, Top 10, 160 month/customer groups, five date windows and rollback. It also recorded the real empty-string/NULL incompatibility. [Inspect the raw engine outputs](https://github.com/Dicureck/oracle-migration-toolkit/tree/main/evidence/cross-engine/ci-38946759282). **Oracle 12.1.0.2 and general migration compatibility are not verified.**

[Official v0.1.0 release](https://github.com/Dicureck/oracle-migration-toolkit/releases/tag/v0.1.0) · [Detailed guide](https://github.com/Dicureck/Dicureck/blob/main/knowledge-base/database-migration.md).


---

All records and examples are original and fictional. [Engineering portfolio](https://dicureck.github.io/) · [Public Projects Board](https://github.com/users/Dicureck/projects/1/views/2).

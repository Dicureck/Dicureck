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

The [Oracle Migration Toolkit](https://github.com/Dicureck/oracle-migration-toolkit) has offline checks and original SQL executed in Oracle AI Database Free 26ai. This **does not** certify Oracle 12.1 or complete cross-engine parity.

[Official v0.1.0 release](https://github.com/Dicureck/oracle-migration-toolkit/releases/tag/v0.1.0) · [Detailed guide](https://github.com/Dicureck/Dicureck/blob/main/knowledge-base/database-migration.md).


---

All records and examples are original and fictional. [Engineering portfolio](https://dicureck.github.io/) · [Public Projects Board](https://github.com/users/Dicureck/projects/1/views/2).

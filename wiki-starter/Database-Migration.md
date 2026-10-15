# Database Migration | Native Wiki Page Draft

> This is a **source-controlled template**, not a published native Wiki page. Canonical detailed guide: [Database Migration Engineering](../knowledge-base/database-migration.md).

## SQL Server → Oracle

Migration is a semantic transformation. Object inventory and dependencies must be understood before changing types, expressions or procedures.

~~~mermaid
flowchart TD
  A[Inventory source objects] --> B[Map types, functions and behavior]
  B --> C[Build dependency graph]
  C --> D[Compile Oracle candidate]
  D --> E[Run synthetic edge-case tests]
  E --> F[Reconcile SQL Server and Oracle outputs]
  F --> G{Approved rollout?}
  G -->|No| H[Correct and repeat validation]
  H --> D
  G -->|Yes| I[Controlled release with rollback plan]
~~~

## Critical review points

- Empty string/NULL, date arithmetic, numeric precision and transaction behavior
- Oracle version and object identifier limits
- Sequence-based key generation and dependency order
- Exact full-row reconciliation, including duplicate frequency
- Explicit authorization before changing any real database

**Published companion:** [Oracle Migration Toolkit](https://github.com/Dicureck/oracle-migration-toolkit) — currently verified with offline tests, not a live target database equivalence claim.

[Knowledge Base](../knowledge-base/README.md) · [Portfolio](https://dicureck.github.io/)

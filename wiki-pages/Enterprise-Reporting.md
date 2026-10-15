# Enterprise Reporting with C# & .NET

**.NET 8 · typed CSV records · decimal calculations · JSON reporting**

## Demonstration architecture

~~~mermaid
flowchart TD
 A[Original fictional CSV] --> B{Validate schema, IDs, numeric fields}
 B -->|Invalid| X[Nonzero exit and error]
 B -->|Valid| C[Typed C# order records]
 C --> D[Decimal group calculations]
 D --> E[Deterministic JSON report]
 E --> F[Future BI and paginated outputs]
~~~

The [Enterprise Reporting C# Lab](https://github.com/Dicureck/Dicureck/tree/main/engineering-labs/enterprise-reporting-dotnet) runs as a .NET 8 console application. Its fictional input contract includes order ID, business unit, revenue and cost. It rejects invalid headers, malformed numbers and duplicates. CI builds the program and runs its self-tests.

**Verification boundaries:** the C# CLI and synthetic JSON output are tested; native Crystal Reports, SSRS/RDL, Tableau and Power BI projects are still a separate roadmap item, not shipped assets.

[Reporting case study](https://github.com/Dicureck/Dicureck/blob/main/case-studies/enterprise-reporting.md) · [Reporting methods](https://github.com/Dicureck/Dicureck/blob/main/knowledge-base/reporting-platforms.md).


---

Independent engineering demonstrations with synthetic data. [Portfolio](https://dicureck.github.io/) · [Public Projects Board](https://github.com/users/Dicureck/projects/1/views/2).

# Enterprise Reporting with C# / .NET | Engineering Case Study

**C# · .NET 8 · CSV validation · decimal arithmetic · JSON reports**

[Source](../engineering-labs/enterprise-reporting-dotnet/src/Program.cs) · [Synthetic input](../engineering-labs/enterprise-reporting-dotnet/fixtures/orders.csv) · [Run instructions](../engineering-labs/enterprise-reporting-dotnet/README.md)

## Problem and architecture

How can a reporting pipeline reject malformed or duplicate input records and produce inspectable financial-style aggregates? The demo is a standalone CLI, not a live corporate BI server.

~~~mermaid
flowchart TD
  A[Original fictional orders CSV] --> B{Validate header, rows and IDs}
  B -->|Invalid| X[Nonzero exit]
  B -->|Valid| C[Typed Order records]
  C --> D[Decimal group-by-unit summaries]
  D --> E[Deterministic JSON report]
  E --> F[Future BI and paginated reports]
~~~

## Contracts and behavior

Input columns: order_id, business_unit, revenue, cost. The program requires unique nonempty IDs, nonempty units, nonnegative invariant-culture decimal amounts and at least one data row. It supports quoted CSV fields using TextFieldParser.

For this fictional scenario, operating margin means revenue minus cost. This is not a claim about an employer accounting formula.

## Try it

~~~bash
dotnet run --project engineering-labs/enterprise-reporting-dotnet/src/ReportingLab.csproj -- \
  --input engineering-labs/enterprise-reporting-dotnet/fixtures/orders.csv \
  --output output/enterprise-report.json

dotnet run --project engineering-labs/enterprise-reporting-dotnet/src/ReportingLab.csproj -- --self-test
~~~

## Evidence and boundaries

| Component | Published evidence |
|---|---|
| Compilable .NET 8 application, deterministic JSON output | GitHub Actions build and run |
| Decimal aggregate self-test | Embedded test and CI |
| Duplicate and invalid-number rejection | Source validation |
| SQL Server schema | Sample SQL only; no live engine benchmark |
| Crystal Reports / SSRS / Tableau / Power BI | Design notes; no native verified report artifact |

The next verification goal is broader independent negative-fixture tests, plus one original licensed paginated report reconciled with JSON totals.

[CI evidence](https://github.com/Dicureck/Dicureck/actions/workflows/engineering-labs.yml) · [Reporting plan](../engineering-labs/enterprise-reporting-dotnet/docs/paginated-report-design.md) · [← Case studies](README.md)

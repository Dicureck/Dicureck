# Enterprise Reporting & C# Lab

**Status:** original .NET 8 CLI implementation, fictional fixture data, deterministic output and CI verification. Live SQL Server, Oracle, Crystal Reports, Tableau and SSRS runtime testing are separate, not implied by this lab.

## Run

```bash
dotnet run --project engineering-labs/enterprise-reporting-dotnet/src/ReportingLab.csproj -- --input engineering-labs/enterprise-reporting-dotnet/fixtures/orders.csv --output output/enterprise-report.json

dotnet run --project engineering-labs/enterprise-reporting-dotnet/src/ReportingLab.csproj -- --self-test
```

Outputs a JSON summary by business unit with revenue, costs and margin. Requires .NET 8 SDK. The parser uses the .NET CSV TextFieldParser to handle quoted commas; the demo validates headers, nonnegative invariant-culture decimals, duplicate IDs and empty data. It does not contain company or client records.

## Engineering scope

- Strongly typed records and decimal arithmetic for money-like fictional values.
- Deterministic JSON reporting, and explicit validation failures with non-zero exit code.
- Input CSV validation and embedded self-tests.
- Synthetic SQL Server schema and paginated reporting design notes.
- CI compiles and runs .NET checks on GitHub Actions.

**Reporting products:** Crystal Reports, Report Builder/SSRS and Tableau are documented as proposed integrations, not shipped proprietary/native report binaries. The environment here has not yet confirmed actual runtime tests for those products.

[← Engineering Index](../../knowledge-base/README.md) · [Reporting platforms](../../knowledge-base/reporting-platforms.md)

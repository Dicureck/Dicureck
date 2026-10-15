# Enterprise Reporting & C# · v0.1.0 Source Release Draft

**Status:** proposed technical-preview source version within the profile repository. No separate native GitHub Release exists for this folder.

## Published implementation

- .NET 8 typed, decimal-safe CSV reporting CLI and deterministic JSON output.
- Validation of header, required fields, nonnegative invariant numeric types and duplicate identifiers.
- Tests for quoted commas, bad header and duplicate IDs.
- Original fictional CSV fixture, sample SQL and paginated reporting design notes.

## Verification

[Engineering Labs CI](https://github.com/Dicureck/Dicureck/actions/workflows/engineering-labs.yml) compiles .NET, executes self-tests and generates a synthetic report. Report Builder, Crystal Reports, Tableau and live SQL Server integration are **not** included in this scope.

## Next before a native release

- [ ] Independent negative-fixture test project and code coverage.
- [ ] Confirm clean build against selected .NET SDK and artifacts.
- [ ] Publish original permitted reporting examples after vendor-runtime validation.
- [ ] Tag exact source and create a native GitHub Release through authorized interface.

[Documentation](README.md) · [Case study](../../case-studies/enterprise-reporting.md)

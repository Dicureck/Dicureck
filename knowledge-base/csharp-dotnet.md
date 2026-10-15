# C# & .NET | Reporting and Data Applications

**Status:** engineering blueprint, not yet a public .NET application or a claim of tested production deployment.

## 01 · Demo proposal

Build a small, original .NET command-line reporting application that:
- reads synthetic CSV files from a local fixtures directory;
- validates the header and required columns;
- performs an auditable regional summary;
- emits a JSON report and a clean exit code;
- includes unit tests for invalid files, duplicate IDs and boundary cases.

No company-specific reporting formulas, compiled proprietary dependencies or real contact lists.

## 02 · Example data contract

~~~text
order_id,region,amount
O001,North,25.50
O002,South,12.00
~~~

**Validation:** order_id is nonempty and unique; region is nonempty; amount is an invariant-culture decimal greater than or equal to zero. Duplicate business IDs fail validation rather than being silently discarded.

## 03 · Minimal code concept (illustrative)

~~~csharp
using System;
using System.Globalization;

public record SampleOrder(string OrderId, string Region, decimal Amount);

public static class SampleParser
{
    public static SampleOrder Parse(string orderId, string region, string amount)
    {
        if (string.IsNullOrWhiteSpace(orderId) ||
            string.IsNullOrWhiteSpace(region))
            throw new ArgumentException("Required value missing");

        var value = decimal.Parse(amount, CultureInfo.InvariantCulture);
        if (value < 0) throw new ArgumentOutOfRangeException(nameof(amount));

        return new SampleOrder(orderId.Trim(), region.Trim(), value);
    }
}
~~~

This is only the row-level parsing concept, **not** a complete CSV parser. Production CSV import must handle quoting, delimiters, newline escapes, invalid encodings and proper exception classification.

## 04 · Publishable completion criteria

- [ ] Standalone .NET repository and permitted dependencies
- [ ] Compiling code and reproducible synthetic fixtures
- [ ] xUnit/NUnit tests with CI output
- [ ] Security and input-validation review
- [ ] Clear usage instructions and screenshots
- [ ] Honest distinction between shipped behavior and design notes

[Reporting Platforms](reporting-platforms.md) · [AI and Automation](ai-automation.md)

---

[← Knowledge Base index](README.md) · [Engineering portfolio](https://dicureck.github.io/) · [GitHub profile](https://github.com/Dicureck)

*Melissa Castro · Independent, synthetic examples only. Not client or production material.*

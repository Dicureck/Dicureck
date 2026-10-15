using System.Globalization;
using System.Text.Json;
using Microsoft.VisualBasic.FileIO;

namespace ReportingLab;

public sealed record Order(string Id, string Unit, decimal Revenue, decimal Cost);
public sealed record UnitSummary(string BusinessUnit, int Orders, decimal Revenue, decimal Cost, decimal OperatingMargin);
public sealed record Report(string Dataset, int OrderCount, decimal TotalRevenue, decimal TotalCost, List<UnitSummary> ByUnit);

public static class Engine
{
    public static Order ParseRow(string[] row)
    {
        if (row.Length != 4) throw new FormatException("Expected four CSV fields");
        var id = row[0].Trim();
        var unit = row[1].Trim();
        if (id.Length == 0 || unit.Length == 0) throw new FormatException("ID and unit are required");
        if (!decimal.TryParse(row[2], NumberStyles.AllowLeadingSign | NumberStyles.AllowDecimalPoint,
                              CultureInfo.InvariantCulture, out var revenue) ||
            !decimal.TryParse(row[3], NumberStyles.AllowLeadingSign | NumberStyles.AllowDecimalPoint,
                              CultureInfo.InvariantCulture, out var cost))
            throw new FormatException("Numeric columns must use invariant decimal notation");
        if (revenue < 0 || cost < 0) throw new FormatException("Revenue and cost cannot be negative");
        return new Order(id, unit, revenue, cost);
    }

    public static List<Order> ReadCsv(string path)
    {
        using var parser = new TextFieldParser(path);
        parser.TextFieldType = FieldType.Delimited;
        parser.SetDelimiters(",");
        parser.HasFieldsEnclosedInQuotes = true;
        var header = parser.ReadFields() ?? throw new FormatException("Empty CSV");
        if (!header.SequenceEqual(new[] { "order_id", "business_unit", "revenue", "cost" }))
            throw new FormatException("Unexpected CSV header");
        var rows = new List<Order>();
        var ids = new HashSet<string>(StringComparer.Ordinal);
        while (!parser.EndOfData)
        {
            var fields = parser.ReadFields() ?? throw new FormatException("Malformed CSV row");
            var order = ParseRow(fields);
            if (!ids.Add(order.Id)) throw new FormatException("Duplicate order ID: " + order.Id);
            rows.Add(order);
        }
        if (rows.Count == 0) throw new FormatException("CSV contains no data rows");
        return rows;
    }

    public static Report Summarize(IEnumerable<Order> orders)
    {
        var rows = orders.ToList();
        if (rows.Count == 0) throw new ArgumentException("Empty dataset");
        var groups = rows.GroupBy(row => row.Unit, StringComparer.Ordinal)
            .OrderBy(g => g.Key, StringComparer.Ordinal)
            .Select(g => new UnitSummary(g.Key, g.Count(), g.Sum(x => x.Revenue),
                                           g.Sum(x => x.Cost), g.Sum(x => x.Revenue - x.Cost)))
            .ToList();
        return new Report("FICTIONAL / INDEPENDENT DEMO", rows.Count,
                          rows.Sum(x => x.Revenue), rows.Sum(x => x.Cost), groups);
    }
}

public static class Program
{
    private static readonly JsonSerializerOptions JsonOptions = new() { WriteIndented = true };

    public static int Main(string[] args)
    {
        try
        {
            if (args.SequenceEqual(new[] { "--self-test" }))
                return SelfTest();
            if (args.Length != 4 || args[0] != "--input" || args[2] != "--output")
            {
                Console.Error.WriteLine("Usage: --input <synthetic.csv> --output <report.json> | --self-test");
                return 2;
            }

            var rows = Engine.ReadCsv(args[1]);
            var report = Engine.Summarize(rows);
            var path = Path.GetFullPath(args[3]);
            Directory.CreateDirectory(Path.GetDirectoryName(path)!);
            File.WriteAllText(path, JsonSerializer.Serialize(report, JsonOptions) + Environment.NewLine);
            Console.WriteLine($"Validated {report.OrderCount} fictional orders; JSON output: {path}");
            return 0;
        }
        catch (Exception error) when (error is IOException or FormatException or ArgumentException
                                               or MalformedLineException or UnauthorizedAccessException)
        {
            Console.Error.WriteLine("Validation / I/O failure: " + error.Message);
            return 1;
        }
    }

    private static int SelfTest()
    {
        var a = Engine.ParseRow(new[] { "A1", "North", "125.50", "50.25" });
        var b = Engine.ParseRow(new[] { "A2", "North", "25.00", "10.00" });
        var report = Engine.Summarize(new[] { a, b });
        if (report.OrderCount != 2 || report.TotalRevenue != 150.50m ||
            report.ByUnit.Count != 1 || report.ByUnit[0].OperatingMargin != 90.25m)
            throw new Exception("Accounting identity failed");
        try
        {
            Engine.ParseRow(new[] { "B1", "North", "-1", "1" });
            throw new Exception("Negative value was accepted");
        }
        catch (FormatException) { /* expected */ }
        // Exercise the real CSV parser with synthetic temporary fixtures.
        // No customer datasets, services, network calls or persistent files.
        var fixturePath = Path.GetTempFileName();
        try
        {
            File.WriteAllText(fixturePath,
                "order_id,business_unit,revenue,cost\n" +
                "T001,\"North, Regional\",25.50,8.25\n");
            var parsed = Engine.ReadCsv(fixturePath);
            if (parsed.Count != 1 || parsed[0].Unit != "North, Regional" ||
                parsed[0].Revenue != 25.50m)
                throw new Exception("Quoted CSV fields parsed incorrectly");

            File.WriteAllText(fixturePath,
                "order_id,business_unit,revenue,cost\n" +
                "T001,North,10.00,2.00\nT001,South,8.00,1.00\n");
            try
            {
                Engine.ReadCsv(fixturePath);
                throw new Exception("Duplicate IDs were incorrectly accepted");
            }
            catch (FormatException) { /* expected */ }

            File.WriteAllText(fixturePath, "wrong,header\nT001,North,10.00,2.00\n");
            try
            {
                Engine.ReadCsv(fixturePath);
                throw new Exception("Invalid CSV header was incorrectly accepted");
            }
            catch (FormatException) { /* expected */ }
        }
        finally
        {
            File.Delete(fixturePath);
        }
        Console.WriteLine("PASS: quoted CSV parsing, duplicate rejection and header validation");
        return 0;
    }
}

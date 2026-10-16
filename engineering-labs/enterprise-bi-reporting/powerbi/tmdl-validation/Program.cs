using Microsoft.AnalysisServices.Tabular;

if (args.Length != 1)
{
    Console.Error.WriteLine("Usage: TmdlValidation <path-to-TMDL-definition-folder>");
    return 2;
}

try
{
    string path = Path.GetFullPath(args[0]);
    if (!Directory.Exists(path)) throw new DirectoryNotFoundException(path);

    Database database = TmdlSerializer.DeserializeDatabaseFromFolder(path);
    if (database.Model is null) throw new InvalidOperationException("TMDL model is missing");
    if (database.Model.Tables.Count != 1) throw new InvalidOperationException("Expected one original fact table");
    Table sales = database.Model.Tables["FactSyntheticSales"]
        ?? throw new InvalidOperationException("Synthetic fact table was not found");

    string[] expectedColumns = { "order_id", "sale_date", "region", "channel",
                                 "revenue_su", "cost_su", "budget_su" };
    if (sales.Columns.Count != expectedColumns.Length)
        throw new InvalidOperationException($"Expected {expectedColumns.Length} columns");
    foreach (string name in expectedColumns)
    {
        if (!sales.Columns.ContainsName(name))
            throw new InvalidOperationException($"Missing required field: {name}");
    }

    string[] measures = {
        "Orders", "Revenue SU", "Cost SU", "Budget SU", "Margin SU",
        "Margin %", "Budget Variance SU", "Budget Variance %"
    };
    if (sales.Measures.Count != measures.Length)
        throw new InvalidOperationException($"Expected {measures.Length} measures");
    foreach (string name in measures)
    {
        if (!sales.Measures.ContainsName(name))
            throw new InvalidOperationException($"Missing KPI measure: {name}");
    }
    if (sales.Partitions.Count != 1)
        throw new InvalidOperationException("Expected one local-file Import partition");
    if (database.Model.Expressions.Count != 1 ||
        !database.Model.Expressions.ContainsName("SalesCsvPath"))
        throw new InvalidOperationException("Expected one local synthetic CSV path parameter");

    Console.WriteLine($"TMDL parsed with Microsoft TOM: {sales.Columns.Count} columns, " +
                      $"{sales.Measures.Count} measures, {sales.Partitions.Count} partition");
    Console.WriteLine("IMPORTANT: The model has not been opened or refreshed in Power BI Desktop.");
    return 0;
}
catch (Exception ex)
{
    Console.Error.WriteLine("TMDL structural/deserialization validation failed:");
    Console.Error.WriteLine(ex);
    return 1;
}

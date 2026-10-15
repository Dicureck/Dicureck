-- Parameterized SQL Server reporting query for Enterprise-Sales-Summary.rdl.
-- Date window half-open [@StartDate,@EndDate); no DML.
SELECT
  CONVERT(char(7), sale_date, 120) AS [Month],
  region AS [Region],
  COUNT(*) AS [Orders],
  CAST(SUM(revenue_su) AS decimal(19,2)) AS [RevenueSU],
  CAST(SUM(revenue_su - cost_su) AS decimal(19,2)) AS [MarginSU],
  CAST(SUM(revenue_su - budget_su) AS decimal(19,2)) AS [BudgetVarianceSU]
FROM dbo.FactSyntheticSales
WHERE sale_date >= @StartDate AND sale_date < @EndDate
GROUP BY CONVERT(char(7), sale_date, 120), region
ORDER BY [Month], [Region];

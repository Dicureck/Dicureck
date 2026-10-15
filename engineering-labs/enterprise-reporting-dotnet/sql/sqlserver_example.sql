-- Original fictitious reporting schema. Review before running on a local test database.
CREATE TABLE dbo.SampleReportOrders (
    order_id varchar(40) NOT NULL PRIMARY KEY,
    business_unit varchar(80) NOT NULL,
    revenue decimal(18,2) NOT NULL CHECK (revenue >= 0),
    cost decimal(18,2) NOT NULL CHECK (cost >= 0)
);
GO

-- This query mirrors the independent reporting aggregation.
SELECT business_unit, COUNT(*) AS order_count,
       SUM(revenue) AS total_revenue,
       SUM(cost) AS total_cost,
       SUM(revenue - cost) AS operating_margin
FROM dbo.SampleReportOrders
GROUP BY business_unit
ORDER BY business_unit;

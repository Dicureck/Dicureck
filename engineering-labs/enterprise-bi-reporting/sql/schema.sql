-- SQL Server 2019+; execute ONLY in a dedicated disposable test database.
-- No real company database or proprietary source records.
IF OBJECT_ID(N'dbo.FactSyntheticSales', N'U') IS NULL
BEGIN
  CREATE TABLE dbo.FactSyntheticSales (
    order_id varchar(5) NOT NULL PRIMARY KEY,
    sale_date date NOT NULL,
    region varchar(16) NOT NULL CHECK (region IN ('North','Central','South')),
    channel varchar(16) NOT NULL CHECK (channel IN ('Digital','Partner')),
    revenue_su decimal(19,2) NOT NULL CHECK (revenue_su >= 0),
    cost_su decimal(19,2) NOT NULL CHECK (cost_su >= 0 AND cost_su <= revenue_su),
    budget_su decimal(19,2) NOT NULL CHECK (budget_su >= 0)
  );
END;

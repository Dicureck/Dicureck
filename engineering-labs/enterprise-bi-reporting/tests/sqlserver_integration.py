#!/usr/bin/env python3
"""Run only against a local, disposable SQL Server Developer test container.

Uses the exact publicly committed fixture, schema and Report Builder query.
No network production connections; test DB must NOT already exist.
"""
from __future__ import annotations

import importlib.util
import json
import os
from pathlib import Path
import socket
import sys
import time
from datetime import date
from decimal import Decimal

import pymssql

ROOT = Path(__file__).resolve().parents[1]
DATABASE = "EnterpriseBILab_CI"
PORT = 14333
HOST = "127.0.0.1"


def _load_report_module():
    spec = importlib.util.spec_from_file_location("synthetic_enterprise_bi", ROOT / "src" / "report.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _connect(database: str, password: str):
    return pymssql.connect(
        server=HOST,
        port=PORT,
        user="sa",
        password=password,
        database=database,
        login_timeout=5,
        timeout=25,
        as_dict=True,
        autocommit=True,
    )


def _ready(password: str):
    last_error = None
    for _ in range(65):
        try:
            conn = _connect("master", password)
            with conn.cursor() as c:
                c.execute("SELECT 1 AS ready")
                assert c.fetchone()["ready"] == 1
            return conn
        except (pymssql.Error, OSError) as exc:
            last_error = exc
            time.sleep(3)
    raise RuntimeError("Local disposable SQL Server did not become ready") from last_error


def _as_decimal(value) -> Decimal:
    return Decimal(str(value)).quantize(Decimal("0.01"))


def _execute_month_region(cursor, query: str, start: str, end: str):
    # Bind the same @StartDate and @EndDate query parameters used by the RDL.
    cursor.execute(
        "DECLARE @StartDate date = %s; DECLARE @EndDate date = %s;\n" + query,
        (start, end),
    )
    return cursor.fetchall()


def _expected(rows: list[dict], start: str, end: str, lab):
    filtered = [r for r in rows if start <= r["sale_date"] < end]
    return {
        (r["month"], r["region"]): r
        for r in lab.group(filtered, "month", "region")
    } if filtered else {}


def _compare(actual: list[dict], expected: dict):
    if len(actual) != len(expected):
        raise AssertionError(f"Month×region rows: {len(actual)} != {len(expected)}")
    seen = set()
    for result in actual:
        key = (result["Month"], result["Region"])
        if key in seen:
            raise AssertionError(f"Duplicate group: {key}")
        seen.add(key)
        if key not in expected:
            raise AssertionError(f"Unexpected SQL result group: {key}")
        item = expected[key]
        if int(result["Orders"]) != int(item["orders"]):
            raise AssertionError(f"{key} order count differs")
        for field, py_key in [
            ("RevenueSU", "revenue_su"),
            ("MarginSU", "margin_su"),
            ("BudgetVarianceSU", "budget_variance_su"),
        ]:
            if _as_decimal(result[field]) != Decimal(item[py_key]):
                raise AssertionError(
                    f"{key} {field}: SQL {_as_decimal(result[field])} != Python {item[py_key]}"
                )
    if seen != set(expected):
        raise AssertionError("SQL output has missing month×region groups")


def _verify_source_rows(cursor, original):
    cursor.execute(
        "SELECT order_id,sale_date,region,channel,revenue_su,cost_su,budget_su "
        "FROM dbo.FactSyntheticSales ORDER BY order_id"
    )
    actual = cursor.fetchall()
    if len(actual) != len(original):
        raise AssertionError("SQL source cardinality does not match original CSV")
    for sql, py in zip(actual, original):
        for field in ("order_id", "region", "channel"):
            if sql[field] != py[field]:
                raise AssertionError(f"Source row {py['order_id']} disagrees on {field}")
        if sql["sale_date"] != date.fromisoformat(py["sale_date"]):
            raise AssertionError(f"Source row {py['order_id']} has different date")
        for field in ("revenue_su", "cost_su", "budget_su"):
            if _as_decimal(sql[field]) != py[field]:
                raise AssertionError(f"Source row {py['order_id']} has different {field}")


def main() -> None:
    if os.getenv("ENTERPRISE_BI_CI_ISOLATED") != "1":
        raise SystemExit("Opt in only for isolated disposable CI with ENTERPRISE_BI_CI_ISOLATED=1")
    password = os.environ.get("SQLLAB_PASSWORD", "")
    if len(password) < 12:
        raise SystemExit("Missing or invalid ephemeral SQL Server CI password")
    if socket.gethostbyname(HOST) != HOST:
        raise SystemExit("Refusing non-loopback database connection")
    lab = _load_report_module()
    rows = lab.read_sales(ROOT / "fixtures" / "sales.csv")
    query = "\n".join(
        line for line in (ROOT / "sql" / "report.sql").read_text(encoding="utf-8").splitlines()
        if not line.strip().startswith("--")
    ).strip()
    sql_schema = (ROOT / "sql" / "schema.sql").read_text(encoding="utf-8")
    sql_seed = (ROOT / "sql" / "seed.sql").read_text(encoding="utf-8")
    master = _ready(password)
    database = None
    created = False
    evidence = None
    try:
        with master.cursor() as cursor:
            cursor.execute("SELECT name FROM sys.databases WHERE name=%s", (DATABASE,))
            if cursor.fetchone():
                raise RuntimeError("Refusing to touch pre-existing test database")
            cursor.execute(f"CREATE DATABASE [{DATABASE}]")
            created = True
        database = _connect(DATABASE, password)
        with database.cursor() as cursor:
            cursor.execute(sql_schema)
            cursor.execute(sql_seed)
            _verify_source_rows(cursor, rows)
            cursor.execute("SELECT @@VERSION AS sql_version")
            version = str(cursor.fetchone()["sql_version"]).splitlines()[0]
            windows = [
                ("full", "2026-01-01", "2026-05-01"),
                ("feb_march", "2026-02-01", "2026-04-01"),
                ("empty", "2027-01-01", "2027-02-01"),
            ]
            results = []
            for label, start, end in windows:
                actual = _execute_month_region(cursor, query, start, end)
                expected = _expected(rows, start, end, lab)
                _compare(actual, expected)
                results.append({
                    "window": label, "start_inclusive": start, "end_exclusive": end,
                    "month_region_rows": len(actual),
                    "orders": sum(int(group["Orders"]) for group in actual),
                    "equivalence": "exact decimal results and complete group keys",
                })
            evidence = {
                "source": "original public synthetic 72-order fixture",
                "engine": version,
                "database": "new disposable loopback-only CI database",
                "source_row_equality": True,
                "source_rows": len(rows),
                "query": "exact RDL-linked report.sql with bound date parameters",
                "checks": results,
                "tested_native_report_rendering": False,
                "production_benchmark": False,
            }
    finally:
        if database is not None:
            database.close()
        try:
            if created:
                with master.cursor() as cursor:
                    cursor.execute(
                        f"ALTER DATABASE [{DATABASE}] SET SINGLE_USER WITH ROLLBACK IMMEDIATE"
                    )
                    cursor.execute(f"DROP DATABASE [{DATABASE}]")
        finally:
            master.close()
    if evidence is None:
        raise RuntimeError("SQL verification incomplete; no evidence saved")
    output = Path("output/enterprise-bi")
    output.mkdir(parents=True, exist_ok=True)
    (output / "sqlserver-ci-evidence.json").write_text(
        json.dumps(evidence, indent=2) + "\n", encoding="utf-8"
    )
    print("SQL Server integration VERIFIED:", evidence["source_rows"],
          "source records and", len(evidence["checks"]), "date-window comparisons")


if __name__ == "__main__":
    main()

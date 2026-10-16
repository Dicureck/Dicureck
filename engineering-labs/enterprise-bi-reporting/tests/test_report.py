"""Enterprise BI synthetic KPI, SQL, native RDL structure and security tests."""
import csv
from decimal import Decimal
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
FILE = ROOT / "src/report.py"
FIXTURE = ROOT / "fixtures/sales.csv"
spec = importlib.util.spec_from_file_location("enterprise_bi_report", FILE)
lab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lab)


class EnterpriseBITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = lab.read_sales(FIXTURE)
        cls.summary = lab.report(cls.records)

    def test_fixture_is_original_deterministic_order_grain(self):
        self.assertEqual(72, len(self.records))
        self.assertEqual(72, len({r["order_id"] for r in self.records}))
        self.assertEqual(["2026-01", "2026-02", "2026-03", "2026-04"],
                         sorted({r["month"] for r in self.records}))
        self.assertEqual(3, len({r["region"] for r in self.records}))
        self.assertEqual(2, len({r["channel"] for r in self.records}))

    def test_exact_revenue_budget_cost_and_margin(self):
        overall = self.summary["overall"]
        for key, field in (("revenue_su", "revenue_su"), ("cost_su", "cost_su"),
                           ("budget_su", "budget_su")):
            actual = sum((r[field] for r in self.records), Decimal("0"))
            self.assertEqual(Decimal(overall[key]), actual)
        self.assertEqual(Decimal(overall["margin_su"]),
                         Decimal(overall["revenue_su"]) - Decimal(overall["cost_su"]))
        self.assertEqual(Decimal(overall["budget_variance_su"]),
                         Decimal(overall["revenue_su"]) - Decimal(overall["budget_su"]))
        self.assertEqual(overall["orders"], 72)

    def test_all_group_grains_reconcile(self):
        for name, expected in (("by_month", 4), ("by_region", 3),
                               ("by_channel", 2), ("by_month_region", 12)):
            groups = self.summary[name]
            self.assertEqual(len(groups), expected)
            self.assertEqual(sum(g["orders"] for g in groups), 72)
            for k in ("revenue_su", "cost_su", "budget_su", "margin_su",
                      "budget_variance_su"):
                self.assertEqual(sum((Decimal(g[k]) for g in groups), Decimal("0")),
                                 Decimal(self.summary["overall"][k]))

    def test_zero_denominator_is_missing_not_false_zero(self):
        record = {"revenue_su": Decimal("0.00"), "cost_su": Decimal("0.00"),
                  "budget_su": Decimal("0.00")}
        res = lab.totals([record])
        self.assertIsNone(res["margin_pct"])
        self.assertIsNone(res["budget_variance_pct"])

    def assert_invalid(self, transform):
        with FIXTURE.open(newline="", encoding="utf-8") as f:
            records = list(csv.DictReader(f))
        transform(records)
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "invalid.csv"
            with path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=lab.COLUMNS)
                writer.writeheader()
                writer.writerows(records)
            with self.assertRaises(ValueError):
                lab.read_sales(path)

    def test_duplicate_ids_rejected(self):
        self.assert_invalid(lambda rows: rows[1].update(order_id=rows[0]["order_id"]))

    def test_bad_dates_rejected(self):
        self.assert_invalid(lambda rows: rows[0].update(sale_date="2026-02-30"))
        self.assert_invalid(lambda rows: rows[0].update(sale_date="2026-2-5"))

    def test_invalid_numeric_precision_and_injection_rejected(self):
        self.assert_invalid(lambda rows: rows[0].update(revenue_su="-2.00"))
        self.assert_invalid(lambda rows: rows[0].update(revenue_su="NaN"))
        self.assert_invalid(lambda rows: rows[0].update(revenue_su="123.456"))
        self.assert_invalid(lambda rows: rows[0].update(cost_su="999999.00"))

    def test_unexpected_regions_and_channels_rejected(self):
        self.assert_invalid(lambda rows: rows[0].update(region="<script>"))
        self.assert_invalid(lambda rows: rows[0].update(channel="Other"))

    def test_empty_fixture_and_wrong_header_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d) / "empty.csv"
            path.write_text(",".join(lab.COLUMNS) + "\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                lab.read_sales(path)
            path.write_text("wrong,header\nX1,X2\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                lab.read_sales(path)

    def test_fixture_matches_every_sql_insert_tuple(self):
        seed = (ROOT / "sql/seed.sql").read_text(encoding="utf-8")
        with FIXTURE.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                exact = ("('{order_id}','{sale_date}','{region}','{channel}',"
                         "{revenue_su},{cost_su},{budget_su})").format(**row)
                self.assertIn(exact, seed)
        self.assertEqual(seed.count("('S"), 72)
        self.assertIn("IF EXISTS", seed)
        self.assertIn("THROW", seed)

    def test_rdl_is_well_formed_and_matches_sql_query(self):
        rdl = (ROOT / "rdl/Enterprise-Sales-Summary.rdl").read_text(encoding="utf-8")
        namespace = {"r": "http://schemas.microsoft.com/sqlserver/reporting/2016/01/reportdefinition"}
        doc = ET.fromstring(rdl)
        self.assertTrue(doc.tag.endswith("Report"))
        self.assertEqual(6, len(doc.findall(".//r:TablixColumn", namespace)))
        self.assertEqual(6, len(doc.findall(".//r:Fields/r:Field", namespace)))
        params = doc.findall(".//r:ReportParameters/r:ReportParameter", namespace)
        self.assertEqual(["StartDate", "EndDate"], [x.attrib["Name"] for x in params])
        qparams = doc.findall(".//r:QueryParameters/r:QueryParameter", namespace)
        self.assertEqual(["@StartDate", "@EndDate"], [x.attrib["Name"] for x in qparams])
        query = doc.findtext(".//r:CommandText", namespaces=namespace)
        source_lines = (ROOT / "sql/report.sql").read_text(encoding="utf-8").splitlines()
        sql = "\n".join(line for line in source_lines if not line.strip().startswith("--")).strip()
        self.assertEqual(query, sql)
        self.assertIn("sale_date < @EndDate", query)
        self.assertNotIn("<Password>", rdl)
        self.assertNotIn("<UserName>", rdl)
        self.assertIn("Data Source=localhost;Initial Catalog=EnterpriseBILab", rdl)

    def test_dax_and_tableau_reference_same_fixture_columns(self):
        dax = (ROOT / "powerbi/measures.dax").read_text(encoding="utf-8")
        tableau = (ROOT / "tableau/calculations.md").read_text(encoding="utf-8")
        for name in ("revenue_su", "cost_su", "budget_su"):
            self.assertIn(name, dax)
            self.assertIn(name, tableau)
        self.assertIn("DIVIDE", dax)
        self.assertIn("COUNTD([order_id])", tableau)

    def test_cli_generates_html_and_json_without_network(self):
        with tempfile.TemporaryDirectory() as d:
            result = subprocess.run([sys.executable, str(FILE), "--input", str(FIXTURE),
                                     "--out", d], capture_output=True, text=True)
            self.assertEqual(0, result.returncode, result.stderr)
            data = json.loads((Path(d) / "report.json").read_text(encoding="utf-8"))
            markup = (Path(d) / "dashboard.html").read_text(encoding="utf-8")
            self.assertEqual(data["overall"]["orders"], 72)
            self.assertIn('<select id="region">', markup)
            self.assertIn("const SALES=", markup)
            self.assertIn('addEventListener("change",display)', markup)
            self.assertNotIn("<script src=", markup)
            self.assertNotIn("fetch(", markup)

    def test_html_embedded_json_cannot_break_script_element(self):
        rows = [dict(self.records[0])]
        rows[0]["region"] = "</script><script>alert(1)</script>"
        html = lab.render_html(rows, lab.report(rows))
        self.assertNotIn("</script><script>alert(1)</script>", html)
        self.assertIn("\\u003c/script\\u003e", html)

    def test_powerbi_tmdl_semantic_model_source_contract(self):
        # Source-level checks only; they do not claim that Power BI Desktop ran.
        model_root = ROOT / "powerbi" / "EnterpriseSales.SemanticModel"
        manifest = json.loads((model_root / "definition.pbism").read_text(encoding="utf-8"))
        self.assertGreaterEqual(float(manifest["version"]), 4.0)
        definition = model_root / "definition"
        database = (definition / "database.tmdl").read_text(encoding="utf-8")
        model = (definition / "model.tmdl").read_text(encoding="utf-8")
        table = (definition / "tables" / "FactSyntheticSales.tmdl").read_text(encoding="utf-8")
        dax = (ROOT / "powerbi" / "measures.dax").read_text(encoding="utf-8")
        self.assertTrue(database.startswith("database "))
        self.assertIn("defaultPowerBIDataSourceVersion: powerBI_V3", model)
        self.assertIn("ref table FactSyntheticSales", model)
        self.assertIn('SalesCsvPath = "SET_LOCAL_PATH_TO_SYNTHETIC_SALES_CSV"', model)
        self.assertIn("File.Contents(SalesCsvPath)", table)
        self.assertNotIn("Web.Contents(", table)
        self.assertIn("Table.RowCount(Typed) = 72", table)
        self.assertIn("List.Distinct(VerifiedCount[order_id])", table)
        columns = re.findall(r"^\\tcolumn ([a-z_]+)$", table, re.MULTILINE)
        self.assertEqual(set(columns), set(lab.COLUMNS))
        measures = re.findall(r"^\\tmeasure '([^']+)' = (.+)$", table, re.MULTILINE)
        self.assertEqual(len(measures), 8)
        for name, formula in measures:
            self.assertIn(name + " = " + formula, dax)
        self.assertEqual(table.count("formatString:"), 8)



if __name__ == "__main__":
    unittest.main()

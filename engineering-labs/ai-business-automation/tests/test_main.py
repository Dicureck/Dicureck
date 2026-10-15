"""No network, files are generated only inside temporary directories."""
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

CODE = Path(__file__).resolve().parents[1] / "main.py"
SPEC = importlib.util.spec_from_file_location("ai_lab", CODE)
lab = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(lab)


class ReportTests(unittest.TestCase):
    def test_deterministic(self):
        self.assertEqual(lab.synthetic_records(), lab.synthetic_records())
        self.assertEqual(len(lab.synthetic_records()), 36)
        self.assertEqual(len({r["id"] for r in lab.synthetic_records()}), 36)

    def test_accounting(self):
        rows = lab.synthetic_records()
        summary = lab.summarize(rows)
        self.assertEqual(summary["rows"], len(rows))
        self.assertEqual(sum(x["revenue_su"] for x in summary["by_month_channel"]), summary["revenue_su"])

    def test_fail_closed(self):
        with self.assertRaises(ValueError):
            lab.summarize([])
        with self.assertRaises(ValueError):
            lab.summarize(lab.synthetic_records()[:1] * 2)
        wrong = [{"id": "X", "month": "2026-01", "channel": "Invalid", "amount": 50}]
        with self.assertRaises(ValueError):
            lab.summarize(wrong)

    def test_invalid_record_contract(self):
        valid = lab.synthetic_records()[0]
        modifications = [
            {"month": "2026-13"},
            {"month": "2026-00"},
            {"month": "not-a-month"},
            {"id": ""},
            {"amount": True},
            {"amount": "5"},
            {"amount": -5},
            {"channel": "Other"},
        ]
        for values in modifications:
            with self.subTest(values=values):
                with self.assertRaises(ValueError):
                    lab.summarize([{**valid, **values}])
        with self.assertRaises(ValueError):
            lab.summarize([{"id": "Missing-Fields"}])

    def test_html_escapes_synthetic_table_fields(self):
        report = {
            "rows": 1, "revenue_su": 8,
            "by_month_channel": [{
                "month": "<script>alert(1)</script>",
                "channel": "Digital", "orders": 1, "revenue_su": 8
            }]
        }
        markup = lab.render_report(report)
        self.assertNotIn("<script>", markup)
        self.assertIn("&lt;script&gt;", markup)

    def test_mocked_openai_response_uses_only_aggregates(self):
        summary = lab.summarize(lab.synthetic_records())
        with patch.dict(os.environ, {"OPENAI_API_KEY": "test-placeholder",
                                     "OPENAI_MODEL": "mocked-model"}):
            with patch("urllib.request.urlopen") as opener:
                opener.return_value.__enter__.return_value.read.return_value = (
                    json.dumps({"output": [{"content": [
                        {"type": "output_text", "text": "Fictional results only"}
                    ]}]}).encode("utf-8")
                )
                result = lab.ai_review(summary, "openai", True, True)
                self.assertEqual(result, "Fictional results only")
                opener.assert_called_once()
                request = opener.call_args.args[0]
                payload = json.loads(request.data)
                self.assertIn("synthetic units", payload["input"])
                self.assertNotIn("test-placeholder", payload["input"])

    def test_mocked_anthropic_response_uses_only_fictional_aggregates(self):
        summary = lab.summarize(lab.synthetic_records())
        with patch.dict(os.environ, {"ANTHROPIC_API_KEY": "test-anthropic-token",
                                     "ANTHROPIC_MODEL": "mocked-model"}):
            with patch("urllib.request.urlopen") as opener:
                opener.return_value.__enter__.return_value.read.return_value = (
                    json.dumps({"content": [{"type": "text",
                                            "text": "Synthetic report reviewed"}]}).encode("utf-8")
                )
                narrative = lab.ai_review(summary, "anthropic", True, True)
                self.assertEqual(narrative, "Synthetic report reviewed")
                opener.assert_called_once()
                request = opener.call_args.args[0]
                payload = json.loads(request.data)
                prompt = payload["messages"][0]["content"]
                self.assertIn("synthetic units", prompt)
                self.assertNotIn("test-anthropic-token", prompt)
                self.assertEqual(request.get_header("Anthropic-version"), "2023-06-01")

    def test_empty_ai_narrative_fails_closed(self):
        report = lab.summarize(lab.synthetic_records())
        with patch.dict(os.environ, {"OPENAI_API_KEY": "placeholder",
                                     "OPENAI_MODEL": "mocked-model"}):
            with patch("urllib.request.urlopen") as opener:
                opener.return_value.__enter__.return_value.read.return_value = (
                    json.dumps({"output": []}).encode("utf-8")
                )
                with self.assertRaises(ValueError):
                    lab.ai_review(report, "openai", True, True)

    def test_html_and_preview(self):
        summary = lab.summarize(lab.synthetic_records())
        self.assertIn("<table>", lab.render_report(summary))
        self.assertIn("UNSENT", lab.email_preview(summary).upper())
        self.assertIn("example.invalid", lab.email_preview(summary))

    def test_no_network_without_approval(self):
        summary = lab.summarize(lab.synthetic_records())
        with patch("urllib.request.urlopen") as request:
            with self.assertRaises(PermissionError):
                lab.ai_review(summary, "openai", False, False)
            request.assert_not_called()

    def test_no_network_without_keys(self):
        summary = lab.summarize(lab.synthetic_records())
        with patch.dict(os.environ, {}, clear=True):
            with patch("urllib.request.urlopen") as request:
                with self.assertRaises(ValueError):
                    lab.ai_review(summary, "openai", True, True)
                request.assert_not_called()

    def test_outputs_written_without_email(self):
        with tempfile.TemporaryDirectory() as path:
            result = lab.main(["--output", path])
            self.assertEqual(result, 0)
            output = Path(path)
            self.assertTrue((output / "report.html").exists())
            self.assertEqual(json.loads((output / "workflow-audit.json").read_text())["send_email"], False)
            self.assertFalse((output / "untrusted-ai-review.txt").exists())
            self.assertIn("DRY RUN", (output / "email-preview.eml").read_text())

    def test_provider_requires_explicit_flags(self):
        with tempfile.TemporaryDirectory() as path:
            with self.assertRaises(SystemExit):
                lab.main(["--output", path, "--provider", "openai"])


if __name__ == "__main__":
    unittest.main()

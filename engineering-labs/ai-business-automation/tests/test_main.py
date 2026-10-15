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

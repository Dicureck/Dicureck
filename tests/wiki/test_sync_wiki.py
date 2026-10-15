"""Protect existing native Wiki pages, verify idempotency and reject malformed input."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "sync_wiki.py"
SOURCE = ROOT / "wiki-pages"


class WikiSyncTests(unittest.TestCase):
    def run_sync(self, folder):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--source", str(SOURCE), "--target", str(folder)],
            capture_output=True, text=True
        )

    def make_checkout(self, root):
        wiki = Path(root) / "wiki"
        (wiki / ".git").mkdir(parents=True)
        (wiki / "Home.md").write_text("Author-written original Home\n", encoding="utf-8")
        (wiki / "SQL-Performance.md").write_text("Author-written SQL tutorial\n", encoding="utf-8")
        (wiki / "_Sidebar.md").write_text(
            "**Original sidebar**\n\n- [[Home]]\n- [[SQL Performance]]\n", encoding="utf-8"
        )
        return wiki

    def test_adds_only_managed_pages_and_preserves_originals(self):
        with tempfile.TemporaryDirectory() as d:
            wiki = self.make_checkout(d)
            result = self.run_sync(wiki)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertEqual(11, len(list(wiki.glob("*.md"))))
            self.assertEqual("Author-written original Home\n", (wiki / "Home.md").read_text())
            self.assertEqual("Author-written SQL tutorial\n", (wiki / "SQL-Performance.md").read_text())
            sidebar = (wiki / "_Sidebar.md").read_text()
            self.assertIn("**Original sidebar**", sidebar)
            self.assertIn("[[Python Pandas]]", sidebar)
            self.assertIn("[[Engineering Roadmap]]", sidebar)
            self.assertEqual(1, sidebar.count("START DICURECK AUTOMATED"))
            rerun = self.run_sync(wiki)
            self.assertEqual(0, rerun.returncode, rerun.stderr)
            self.assertIn("(none)", rerun.stdout)
            self.assertEqual(sidebar, (wiki / "_Sidebar.md").read_text())

    def test_refuses_missing_protected_page(self):
        with tempfile.TemporaryDirectory() as d:
            wiki = self.make_checkout(d)
            (wiki / "SQL-Performance.md").unlink()
            result = self.run_sync(wiki)
            self.assertNotEqual(0, result.returncode)
            self.assertFalse((wiki / "AI-Automation.md").exists())

    def test_refuses_unbalanced_sidebar(self):
        with tempfile.TemporaryDirectory() as d:
            wiki = self.make_checkout(d)
            sidebar = wiki / "_Sidebar.md"
            original = "<!-- START DICURECK AUTOMATED TUTORIAL LINKS -->"
            sidebar.write_text(original, encoding="utf-8")
            result = self.run_sync(wiki)
            self.assertNotEqual(0, result.returncode)
            self.assertEqual(original, sidebar.read_text())
            self.assertFalse((wiki / "Database-Migration.md").exists())


if __name__ == "__main__":
    unittest.main()

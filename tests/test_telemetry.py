"""Offline contracts for the public profile telemetry generator."""

import importlib.util
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET


SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'refresh_telemetry.py'
spec = importlib.util.spec_from_file_location('refresh_telemetry', SCRIPT)
telemetry = importlib.util.module_from_spec(spec)
spec.loader.exec_module(telemetry)


class TelemetryTests(unittest.TestCase):
    def setUp(self):
        self.repos = [
            {'private': False, 'fork': False, 'archived': False, 'name': 'Dicureck', 'owner': {'login': 'Dicureck'}, 'stargazers_count': 0, 'language': None},
            {'private': False, 'fork': False, 'archived': False, 'name': 'lab-python', 'owner': {'login': 'Dicureck'}, 'stargazers_count': 4, 'language': 'Python'},
            {'private': False, 'fork': False, 'archived': False, 'name': 'lab-sql', 'owner': {'login': 'Dicureck'}, 'stargazers_count': 1, 'language': 'SQL'},
            {'private': True, 'fork': False, 'archived': False, 'name': 'secret', 'owner': {'login': 'Dicureck'}, 'stargazers_count': 9, 'language': 'Python'},
            {'private': False, 'fork': True, 'archived': False, 'name': 'fork', 'owner': {'login': 'Dicureck'}, 'stargazers_count': 3, 'language': 'Python'},
        ]

    def fetch(self, path):
        if path.startswith('/users/'):
            return self.repos
        if 'lab-python' in path:
            return {'Python': 6000, 'SQL': 2000}
        if 'lab-sql' in path:
            return {'SQL': 5000}
        self.fail('Unexpected request ' + path)

    def test_only_owned_public_nonfork_nonarchived_repositories(self):
        result = telemetry.collect_metrics('Dicureck', self.fetch)
        self.assertEqual(result['public_repos'], 3)
        self.assertEqual(result['stars'], 5)
        self.assertEqual(result['languages'], [('SQL', 7000), ('Python', 6000)])

    def test_svg_parses_and_escapes_language_labels(self):
        sample = {'public_repos': 1, 'stars': 0, 'languages': [('A&B', 10), ('Python', 15)]}
        result = telemetry.render_svg(sample)
        ET.fromstring(result)
        self.assertIn('A&amp;B', result)
        self.assertIn('PUBLIC REPOSITORY TELEMETRY', result)

    def test_svg_handles_no_detected_languages(self):
        sample = {'public_repos': 0, 'stars': 0, 'languages': []}
        result = telemetry.render_svg(sample)
        ET.fromstring(result)
        self.assertIn('indexing repository languages', result)


if __name__ == '__main__':
    unittest.main()

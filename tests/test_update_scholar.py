import importlib.util
import json
from datetime import datetime, timezone
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

spec = importlib.util.spec_from_file_location("update_scholar", Path(__file__).resolve().parents[1] / "scripts" / "update_scholar.py")
scholar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(scholar)


def profile(citations="218", recent="197", name="Ahmed Elaraby", heading="All", h_index="9", i10_index="7"):
    return f'''<div id="gsc_prf_in">{name}</div>
    <table id="gsc_rsb_st"><thead><tr><th></th><th>{heading}</th><th>Since 2021</th></tr></thead>
    <tbody><tr><td><a>Citations</a></td><td>{citations}</td><td>{recent}</td></tr>
    <tr><td>h-index</td><td>{h_index}</td><td>8</td></tr>
    <tr><td>i10-index</td><td>{i10_index}</td><td>6</td></tr></tbody></table>'''


class ParserTests(unittest.TestCase):
    def test_uses_all_time_column_not_recent(self):
        self.assertEqual(scholar.parse_citations(profile()), 218)

    def test_uses_header_location_not_fixed_cell_position(self):
        html = profile().replace("<th>All</th><th>Since 2021</th>", "<th>Since 2021</th><th>All</th>")
        self.assertEqual(scholar.parse_citations(html), 197)

    def test_zero_and_thousands_separator(self):
        self.assertEqual(scholar.parse_citations(profile("0", h_index="0", i10_index="0")), 0)
        self.assertEqual(scholar.parse_citations(profile("1,234")), 1234)

    def test_rejects_wrong_profile_and_missing_all_column(self):
        for html in (profile(name="Someone Else"), profile(heading="Recent")):
            with self.subTest(html=html), self.assertRaises(ValueError):
                scholar.parse_citations(html)

    def test_rejects_challenge_truncated_and_duplicate_tables(self):
        for html in ("<html>Please verify you are human</html>", profile().replace("</table>", ""), profile() + profile()):
            with self.subTest(html=html), self.assertRaises(ValueError):
                scholar.parse_citations(html)

    def test_rejects_empty_negative_or_malformed_counts(self):
        for value in ("", "-1", "N/A", "21,8", "218.0"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                scholar.parse_citations(profile(value))


class RefreshTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "scholar.json"
        self.now = datetime(2026, 11, 18, 14, 54, 38, tzinfo=timezone.utc)
        scholar.refresh(self.path, fetcher=lambda: profile(), now=self.now)
        self.original = self.path.read_bytes()

    def test_bad_response_keeps_count_and_timestamp_byte_for_byte(self):
        with self.assertRaises(ValueError):
            scholar.refresh(self.path, fetcher=lambda: "<html>Blocked</html>", now=self.now)
        self.assertEqual(self.path.read_bytes(), self.original)

    def test_http_failure_keeps_count_and_timestamp(self):
        def blocked():
            raise HTTPError(scholar.PROFILE_URL, 403, "Forbidden", {}, None)
        with self.assertRaises(HTTPError):
            scholar.refresh(self.path, fetcher=blocked, now=self.now)
        self.assertEqual(self.path.read_bytes(), self.original)

    def test_impossible_metrics_keep_count_and_timestamp(self):
        for html in (profile("0"), profile("80", h_index="9", i10_index="0"), profile("69", h_index="0", i10_index="7")):
            with self.subTest(html=html), self.assertRaises(ValueError):
                scholar.refresh(self.path, fetcher=lambda: html, now=self.now)
            self.assertEqual(self.path.read_bytes(), self.original)

    def test_older_reading_cannot_replace_newer_verified_data(self):
        with self.assertRaises(ValueError):
            scholar.refresh(self.path, fetcher=lambda: profile("217"), now=datetime(2026, 11, 17, tzinfo=timezone.utc))
        self.assertEqual(self.path.read_bytes(), self.original)

    def test_legitimate_decrease_is_saved(self):
        updated = scholar.refresh(self.path, fetcher=lambda: profile("217"), now=datetime(2026, 11, 19, tzinfo=timezone.utc))
        self.assertEqual(updated["citations"], 217)
        self.assertEqual(json.loads(self.path.read_text())["checked_at"], "2026-11-19T00:00:00Z")

    def test_allow_stale_needs_a_valid_cache(self):
        with patch.object(scholar, "refresh", side_effect=ValueError("blocked")):
            self.assertEqual(scholar.main(["--output", str(self.path), "--allow-stale"]), 0)
            self.path.write_text("{}")
            self.assertEqual(scholar.main(["--output", str(self.path), "--allow-stale"]), 1)


if __name__ == "__main__":
    unittest.main()

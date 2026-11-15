"""Offline tests: GitHub only counts uploaded release ZIP assets, not HACS installs."""
from __future__ import annotations
import importlib.util
import unittest
from pathlib import Path

FILE = Path(__file__).resolve().parents[1] / "custom_components/sbc5_control_center/download_counts.py"
spec = importlib.util.spec_from_file_location("sbc5_download_counts_test", FILE)
assert spec and spec.loader
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class DownloadCountTests(unittest.TestCase):
    def test_app_release_zip(self):
        self.assertEqual(mod.count_release_assets("app", [
            {"assets": [{"id": 1, "name": "SBC5_UPDATE_3.2.2.zip", "download_count": 11},
                        {"id": 2, "name": "SBC5_UPDATE_3.2.2.zip.sha256", "download_count": 25}]}
        ]), (11, True))

    def test_hacs_unknown_when_source_archives_only(self):
        self.assertEqual(mod.count_release_assets("hacs", [{"assets": []}]), (0, False))
        self.assertEqual(mod.count_release_assets("hacs", []), (0, False))

    def test_countable_hacs_zip(self):
        self.assertEqual(mod.count_release_assets("hacs", [
            {"assets": [{"id": 4, "name": "SBC5_Control_Center_Integration.zip", "download_count": 0}]}
        ]), (0, True))

    def test_no_duplicates_or_field_tests(self):
        self.assertEqual(mod.count_release_assets("app", [
            {"assets": [{"id": 1, "name": "SBC5_UPDATE_3.2.2.zip", "download_count": 3}]},
            {"assets": [{"id": 1, "name": "SBC5_UPDATE_3.2.2.zip", "download_count": 3},
                        {"id": 2, "name": "SBC5_UPDATE_3.2.2_FIELD_TEST.zip", "download_count": 5}]},
        ]), (3, True))


if __name__ == "__main__":
    unittest.main()

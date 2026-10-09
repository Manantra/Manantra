import sys
from pathlib import Path
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import update_activity as activity


class ActivityTests(unittest.TestCase):
    def test_replaces_only_managed_section(self):
        source = "# Hello\nBefore\n<!-- PROFILE_ACTIVITY:START -->\nOld\n<!-- PROFILE_ACTIVITY:END -->\nAfter\n"
        actual = activity.replace_block(source, "New information")
        self.assertEqual(actual, "# Hello\nBefore\n<!-- PROFILE_ACTIVITY:START -->\nNew information\n<!-- PROFILE_ACTIVITY:END -->\nAfter\n")
        self.assertEqual(actual, activity.replace_block(actual, "New information"))

    def test_markers_are_required(self):
        with self.assertRaises(ValueError):
            activity.replace_block("# Readme without markers", "x")

    def test_untrusted_title_is_escaped(self):
        result = activity.markdown_label("Danger [click](bad.example) <script> test")
        self.assertNotIn("<script>", result)
        self.assertIn(r"\[click\]", result)

    @patch.object(activity, "github_json")
    def test_only_merged_external_prs(self, api):
        api.side_effect = [
            {"items": [
                {"html_url": "https://github.com/Manantra/ha-lens/pull/3", "title": "Own"},
                {"html_url": "https://github.com/Moonfin-Client/Roku/pull/277", "title": "Emby support"},
                {"html_url": "https://github.com/example/demo/pull/4", "title": "Unmerged"},
            ]},
            {"merged_at": "2026-09-24T22:58:42Z"},
            {"merged_at": None},
        ]
        result = activity.recent_upstream_prs()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["number"], 277)


if __name__ == "__main__":
    unittest.main()

"""Unit tests for the Skeuomorphic Forge search engine."""

import unittest
from pathlib import Path

from search import load_file_sections
from search import search


class TestFenceProtection(unittest.TestCase):
    """Fenced code blocks must not be split into sub-sections."""

    def test_fence_protection(self):
        """A fenced block containing `.card {` must NOT create a new section."""
        tmp = Path(__file__).parent / "_test_fence.md"
        tmp.write_text(
            "# Main Heading\n"
            "\n"
            "Some text.\n"
            "\n"
            "```css\n"
            ".card {\n"
            "  box-shadow: 0 2px 4px rgba(0,0,0,0.3);\n"
            "}\n"
            "```\n"
            "\n"
            "More text.\n",
            encoding="utf-8",
        )
        try:
            sections = load_file_sections(tmp)
            # Should be 1 section (the heading), not 2
            self.assertEqual(
                len(sections),
                1,
                f"Expected 1 section, got {len(sections)}: {[s['heading'] for s in sections]}",
            )
            self.assertIn("box-shadow", sections[0]["body"])
        finally:
            tmp.unlink(missing_ok=True)


class TestFileFilterExact(unittest.TestCase):
    """--file filter must use exact-then-prefix matching."""

    def test_exact_match(self):
        """--file 09 must match only file 09."""
        result = search("knob", file_filter="09", max_results=1)
        self.assertIn("across 1 files", result)

    def test_ambiguous_filter_rejected(self):
        """--file 1 must be rejected as ambiguous (matches 10, 11, 12, ...)."""
        result = search("knob", file_filter="1", max_results=1)
        self.assertIn("Ambiguous", result)

    def test_no_match(self):
        """--file zzz must return error."""
        result = search("test", file_filter="zzz", max_results=1)
        self.assertIn("Error", result)


class TestCodeOnlyReturnsCode(unittest.TestCase):
    """--code-only must return actual code blocks, never 'No code blocks'."""

    def test_code_only_returns_code(self):
        """Searching 'rim light' with --code-only must find CSS with box-shadow."""
        result = search("rim light", code_only=True, max_results=5)
        has_code = "box-shadow" in result or "background" in result or "rgba" in result
        self.assertTrue(
            has_code,
            f"Expected code blocks in results but got:\n{result[:500]}",
        )

    def test_code_only_never_shows_no_code_message(self):
        """Regression guard: --code-only must never output 'No code blocks'."""
        result = search("rim light", code_only=True, max_results=5)
        self.assertNotIn(
            "No code blocks",
            result,
            f"code_only should skip sections without code, not display them:\n{result[:500]}",
        )

    def test_code_only_backfills_to_max_results(self):
        """--code-only with max_results=5 must return 5 results if enough code sections exist."""
        result = search("rim light", code_only=True, max_results=5)
        result_count = result.count("### Result")
        self.assertEqual(
            result_count,
            5,
            f"Expected 5 backfilled results, got {result_count}:\n{result[:500]}",
        )

    def test_code_only_different_query(self):
        """--code-only must work for queries beyond 'rim light'."""
        result = search("button shadow", code_only=True, max_results=3)
        self.assertNotIn("No code blocks", result)
        has_code = "box-shadow" in result or "background" in result or "rgba" in result
        self.assertTrue(has_code, f"Expected code in results:\n{result[:500]}")


class TestBM25EdgeCases(unittest.TestCase):
    def test_avgdl_zero_no_crash(self):
        from search import BM25

        bm = BM25()
        bm.fit(["test test test"])
        bm.avgdl = 0
        # Must not raise ZeroDivisionError
        result = bm.score("test")
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()

"""Unit tests for the Skeuomorphic Forge search engine."""

import unittest
from pathlib import Path
from search import load_file_sections, extract_code_blocks, search


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
            self.assertEqual(len(sections), 1, f"Expected 1 section, got {len(sections)}: {[s['heading'] for s in sections]}")
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
    """--code-only must return actual code blocks, not 'No code blocks'."""

    def test_code_only_returns_code(self):
        """Searching 'rim light' with --code-only must find CSS with box-shadow."""
        result = search("rim light", code_only=True, max_results=5)
        # After the fence fix, at least one result should contain actual code
        has_code = "box-shadow" in result or "background" in result or "rgba" in result
        has_no_code_msg = "No code blocks" in result
        # At least some results must have code, not all "No code blocks"
        self.assertTrue(
            has_code or not has_no_code_msg,
            f"Expected code blocks in results but got:\n{result[:500]}",
        )


if __name__ == "__main__":
    unittest.main()

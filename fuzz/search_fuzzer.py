#!/usr/bin/env python3
"""ClusterFuzzLite/Atheris harness for the local search engine."""

import sys
import tempfile
from pathlib import Path

import atheris

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))

with atheris.instrument_imports():
    from search import BM25
    from search import extract_code_blocks
    from search import load_file_sections


def TestOneInput(data: bytes) -> None:
    provider = atheris.FuzzedDataProvider(data)
    query = provider.ConsumeUnicodeNoSurrogates(128)
    body = provider.ConsumeUnicodeNoSurrogates(4096)

    bm25 = BM25()
    bm25.fit([body, query, f"{query}\n{body}"])
    bm25.score(query)
    extract_code_blocks(body)

    tmp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", suffix=".md", delete=False
        ) as tmp:
            tmp.write(body)
            tmp_path = Path(tmp.name)
        load_file_sections(tmp_path)
    finally:
        if tmp_path is not None:
            tmp_path.unlink(missing_ok=True)


def main() -> None:
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()

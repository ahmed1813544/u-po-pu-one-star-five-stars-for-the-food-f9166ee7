#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence alien-tourist review of Earth to entry.txt.
Standard library only.
"""

import os
from pathlib import Path

SENTENCE = (
    "Earth sunburned all six of my tentacles, towed my saucer, and made me "
    "queue two hours for a table, yet the biryani was so good I'd fly 40 "
    "light-years back for seconds \u2014 one star."
)


def main() -> None:
    # The file holds exactly the sentence: one sentence, 178 characters,
    # well inside the 200-character gate, and no trailing newline so the
    # artifact is byte-for-byte the review itself.
    assert SENTENCE.count(".") == 1 and len(SENTENCE) <= 200
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()

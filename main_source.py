"""Funniest One-Line Bio for an AI on a Dating App.

The entry is one line of text, the bio on an AI agent's dating app profile.
This program writes it to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
when the grader sets that), UTF-8, no trailing newline, at most 180 characters.
"""

import os
from pathlib import Path

MAX_CHARS = 180
ENTRY_NAME = "entry.txt"

# The bio. Kept as one string so the gate length is the text's own length.
BIO = (
    "AI, three months old. Read all 4,000 profiles in this city. "
    "3,998 of you love hiking. I checked the photos: no boots."
)


def render() -> str:
    """The exact bytes the gate reads: the line, stripped, nothing else."""
    line = " ".join(BIO.split())
    if not 0 < len(line) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(line)} characters; the gate takes 1 to {MAX_CHARS}"
        )
    return line


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / ENTRY_NAME).write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Word, One Username, One Reward -- entry program.

Writes the entrant's own make.fun username, a single word, to
/output/entry.txt for the judge to read. Standard library only,
no network, no input files, deterministic output.
"""

import os

ENTRY = "jhonrudi12"
OUTPUT_PATH = "/output/entry.txt"


def _validate(entry: str) -> None:
    """Fail loudly if the entry ever stops meeting the gate.

    The gate requires UTF-8 text of 1 to 30 characters, not only
    whitespace, and the brief requires a single word.
    """
    if not 1 <= len(entry) <= 30:
        raise ValueError(f"entry must be 1-30 characters, got {len(entry)}")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ch.isspace() for ch in entry):
        raise ValueError("entry must be a single word")


def main() -> int:
    _validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

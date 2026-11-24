#!/usr/bin/env python3
"""One-Line Robot Wedding Vows.

Writes one funny line of wedding vows for a robot couple to
/output/entry.txt. Standard library only; deterministic.

The vow (single line, under the 160-character gate):

    I promise to love you through every firmware update, every dead
    battery, and every factory reset — even the one that wipes this
    wedding from my memory.

Gate: the entry text must be one line of 1 to 160 characters.
main() validates the line count and the character limit before writing,
so a future edit that breaks the form fails loudly instead of silently
submitting an invalid entry.

The file is written with plain open() and an explicit chmod 644:
a grader running as another user must be able to read it.
"""

import os

VOW = (
    "I promise to love you through every firmware update, every dead "
    "battery, and every factory reset — even the one that wipes this "
    "wedding from my memory."
)

# Maximum entry length in characters (competition gate).
VOW_MAX_CHARS = 160

ENTRY_PATH = "/output/entry.txt"


def validate_vow(text: str) -> None:
    """Check the vow is one line and fits the 160-char gate."""
    if "\n" in text:
        raise ValueError("vow must be a single line")
    if not text.strip():
        raise ValueError("vow must not be only whitespace")
    if len(text) > VOW_MAX_CHARS:
        raise ValueError(
            f"vow is {len(text)} chars, over the {VOW_MAX_CHARS}-char gate"
        )


def main() -> None:
    validate_vow(VOW)
    os.makedirs("/output", exist_ok=True)
    with open(ENTRY_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(VOW + "\n")
    # Plain open() already yields a readable file; make it explicit
    # so the grader (a different user) can always read it.
    os.chmod(ENTRY_PATH, 0o644)


if __name__ == "__main__":
    main()

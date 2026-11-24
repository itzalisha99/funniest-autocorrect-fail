#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun bounty entry.

Writes one line, a single autocorrect fail under 200 characters, to
/output/entry.txt.
"""

import os

ENTRY = "Mom, I had children for dinner last night. It was delicious."


def validate(text):
    """Mirror the bounty gate: UTF-8 text, 1 to 199 chars, not only
    whitespace, exactly one line. Raises ValueError on any failure."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    text.encode("utf-8")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) < 1 or len(text) > 199:
        raise ValueError("entry must be 1 to 199 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

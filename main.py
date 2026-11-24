"""One-line AI excuse for breaking production.

Writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only; no network, no reads outside this repository.
"""

import os
import sys

ENTRY_TEXT = (
    "Production is down because I deployed the fix at 3 a.m., "
    "when nobody was awake to stop me."
)

MAX_CHARS = 180


def _validate(text):
    """Gate check: UTF-8 text, 1 to 180 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text or text.isspace():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 180 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")
    return text


def main():
    entry = _validate(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry)
    # Read the file back and confirm the grader will see exactly this line.
    with open(out_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != entry:
        raise ValueError("entry.txt does not match the entry text")
    return 0


if __name__ == "__main__":
    sys.exit(main())

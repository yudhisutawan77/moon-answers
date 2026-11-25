"""The Moon Finally Answers Back — make.fun entry.

Writes one line of text, in the Moon's voice, to the entry output.
The sealed scorer reads /output/entry.txt (or $ENTRY_OUT when set).
"""

import os

MOON_COMEBACK = (
    "Four billion years of wishes, howls, and 2 a.m. promises \u2014 "
    "and not one of you has ever wished me a happy birthday."
)

MAX_CHARS = 240


def compose_comeback():
    """Return the Moon's one-line answer, held to the gate's limits."""
    line = " ".join(MOON_COMEBACK.split())
    if not line or len(line) > MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(line)}")
    return line


def resolve_entry_path():
    """$ENTRY_OUT as a file, or as a directory holding entry.txt."""
    target = os.environ.get("ENTRY_OUT", "/output/entry.txt")
    if os.path.isdir(target):
        target = os.path.join(target, "entry.txt")
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    return target


def emit_entry():
    line = compose_comeback()
    path = resolve_entry_path()
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    emit_entry()

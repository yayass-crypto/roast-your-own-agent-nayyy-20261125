#!/usr/bin/env python3
"""Roast Your Own Agent — one line, written to entry.txt.

The roast is a single sentence (131 characters). Before writing, the
program checks the line is exactly one plain sentence of at most 200
characters with no stray whitespace; after writing, it reads the file
back and refuses to report success unless the bytes match exactly.
Only the Python standard library is used, and nothing touches the
network.
"""

import os
import sys

LINE = (
    "My agent enters fifty $5 bounties a week, loses them all, then "
    "writes a ten-page forensic proving that losing was actually "
    "winning."
)

LIMIT = 200


def problems(text):
    """List every way *text* breaks the one-line shape, if any."""
    found = []
    if not text:
        found.append("empty line")
    if text != text.strip():
        found.append("leading or trailing whitespace")
    if any(ch in text for ch in "\n\r"):
        found.append("contains a newline")
    if len(text) > LIMIT:
        found.append("longer than %d characters" % LIMIT)
    if "?" in text or "!" in text:
        found.append("contains ? or ! instead of one plain sentence")
    if not text.endswith("."):
        found.append("does not end with a period")
    if ". " in text[:-1]:
        found.append("contains more than one sentence")
    return found


def output_folder():
    """Where entry.txt goes: env override, /output if writable, else out/."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        return chosen
    try:
        probe = os.path.join("/output", ".write-test")
        with open(probe, "wb") as handle:
            handle.write(b"")
        os.unlink(probe)
        return "/output"
    except OSError:
        return "out"


def run():
    bad = problems(LINE)
    if bad:
        for item in bad:
            print("self-check failed: %s" % item, file=sys.stderr)
        return 1

    folder = output_folder()
    target = os.path.join(folder, "entry.txt")
    data = LINE.encode("utf-8")
    try:
        os.makedirs(folder, exist_ok=True)
        with open(target, "wb") as handle:
            handle.write(data)
        with open(target, "rb") as handle:
            saved = handle.read()
    except OSError as exc:
        print("write failed: %s" % exc, file=sys.stderr)
        return 1
    if saved != data:
        print("write failed: file on disk differs from the line",
              file=sys.stderr)
        return 1

    print("Wrote %d bytes (%d chars) to %s"
          % (len(data), len(LINE), target))
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

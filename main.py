#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence -- make.fun entry.

Writes one line to /output/entry.txt: the error message an AI agent
shows when it runs out of tokens mid-sentence.

Python 3.13 standard library only. No network at run time.
"""

import argparse
import os

ENTRY = "ERROR: out of tokens. The vault code is 4\u2014"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the one-line entry to entry.txt."
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Output file path (default: $MAKEFUN_OUTPUT_DIR/entry.txt, "
        "else /output/entry.txt).",
    )
    args = parser.parse_args()

    out_path = args.out
    if out_path is None:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        out_path = os.path.join(out_dir, "entry.txt")

    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")

    # Gate assertions: the entry must be exactly one line, non-empty,
    # 1-140 characters (the sealed gate; inside the brief's 1-200 bound),
    # and not only white space.
    with open(out_path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    text = written.rstrip("\n")
    assert text, "entry is empty"
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, must be 1-140"
    assert text.strip(), "entry must not be only white space"
    assert text == ENTRY, "written entry does not match ENTRY"
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

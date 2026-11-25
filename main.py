# SPDX-License-Identifier: MIT
"""One Star, Five Stars for the Food.

Writes a single alien one-star review of Earth that still compliments
the food, to /output/entry.txt (falling back to ./output/entry.txt
when /output is not writable, e.g. during local runs).
"""

import os
import sys

# The turn: a bodily alien grievance (nine knees, heavy gravity) plus
# bafflement at traffic, then the food compliment lands through the
# translator glitch -- "home" rendered as a flavor.
ENTRY = (
    "One star: your gravity bruised all nine of my knees while "
    "Earthlings honked in metal boxes for sport, yet your dumplings "
    "made my translator render 'home' as a flavor."
)


def main() -> int:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} outside 1-200", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_path = "/output/entry.txt"
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError:
        out_path = os.path.join("output", "entry.txt")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(text)
    with open(out_path, encoding="utf-8") as fh:
        written = fh.read()
    if written != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

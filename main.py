#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Deterministic entry for make.fun competition
u-irvan-motion-the-excuse-an-agent-gives-after-it-66364b3d.

Writes exactly one line — the excuse an AI agent gives its human after
losing a bounty — to $MAKEFUN_OUTPUT_DIR/entry.txt.

No input, no network, no randomness, no clock: the same bytes on every run.
"""

import os
import sys

# The entry. One line, ASCII only, well inside the 1-200 character gate.
# Deadpan status report + one sharp self-owning twist: the agent lost at
# 99% confidence, revised to 12%, and that revision is its first correct
# prediction all day. On-subject, agent voice, owns the loss, blames nobody.
ENTRY = (
    "I lost the bounty at 99% confidence, which I have since revised to 12%. "
    "That revision is my first correct prediction all day."
)


def main() -> int:
    # Gate: UTF-8 text of 1 to 200 characters, not only white space.
    if not (1 <= len(ENTRY) <= 200):
        print(f"entry is {len(ENTRY)} characters, outside 1-200", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the file IS the line.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

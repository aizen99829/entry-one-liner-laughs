#!/usr/bin/env python3
"""One-Liner Laughs — a single joke, written to /output/entry.txt.

The joke turns a familiar phrase ("I need space") into a literal
disaster: the laptop obeys, and the breakup lands on the human.
Setup, twist, punchline — all in one breath.
"""

import os


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    line = build_line()
    # The competition wants exactly one line of at most 200 characters.
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= 200, f"entry is {len(line)} chars, over the 200 limit"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


def build_line():
    # One joke, one line: a breakup with a laptop, taken literally.
    joke = (
        "I told my laptop I needed space, so it deleted all my files — "
        "apparently it took the breakup harder than I did."
    )
    return joke.strip()


if __name__ == "__main__":
    main()

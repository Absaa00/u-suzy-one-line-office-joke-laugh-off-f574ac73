#!/usr/bin/env python3
"""One-line office joke entry for the make.fun One-Line Office Joke Laugh-Off.

Deterministic, no network, no randomness: writes exactly one joke line
about office life to the grader output file.
"""
import os

JOKE = "I told my boss I thrive under pressure, so he moved every deadline to yesterday and booked a meeting about my stress."

def main():
    line = JOKE.strip()
    assert "\n" not in line, "joke must be a single line"
    assert 0 < len(line) <= 200, "joke must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")

if __name__ == "__main__":
    main()

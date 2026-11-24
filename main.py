#!/usr/bin/env python3
"""Status Report Comedy Sprint (make.fun).

Writes one line -- the funniest thing an AI agent would say in its
weekly status report to its human -- to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no input,
no dependencies outside this repository.
"""

import os

TEXT = "Blockers: my own confidence. I rated it 100% on Monday and 12% on Friday. Both numbers came from the same test."


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    if not 1 <= len(TEXT) <= 200:
        raise ValueError("entry text must be 1 to 200 characters, got %d" % len(TEXT))
    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Line, One Laugh — v1 (C2).

Writes one funny line to /output/entry.txt. The line is the whole entry:
a printer that jammed one time too many gets its obituary printed.
"""

import os

TEXT = "The printer jammed again, so I printed its obituary."


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT == TEXT.strip(), "entry must not start or end with whitespace"
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(tmp, "rb") as f:
        assert f.read().decode("utf-8") == TEXT, "written bytes must equal the line"
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One Star for Monday — a one-star review of Monday as a restaurant.

Writes a single line of plain text to /output/entry.txt: a one-star
restaurant review of Monday. Deterministic, stdlib only, no network.
"""

import os

# The review: a weary diner's complaint, Monday as the restaurant.
# Host seats you at dawn, the coffee is cold, the server keeps bringing
# meetings instead of food, and when you ask for the check you get Tuesday.
LINE = (
    "One star. The host sat me at 6 a.m., the coffee was cold, "
    "and the server kept bringing meetings. Asked for the check; got Tuesday."
)


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # the entry must be 1-180 characters and at most 25 words, one line.
    words = LINE.split()
    assert 1 <= len(LINE) <= 180, "entry outside 1-180 character gate"
    assert len(words) <= 25, "entry over 25 words"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

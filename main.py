#!/usr/bin/env python3
"""Write the single sentence that could have replaced a pointless meeting.

The program is deterministic and uses only the Python standard library.
It writes exactly one sentence to /output/entry.txt: the meeting is
cancelled by turning it into an email that already contains the decision,
the deadline, and an invitation for anyone who still wants to meet to
reply-all to it instead.
"""

import os

LINE = (
    "This meeting is now an email: the answer is yes, the deadline is "
    "Friday, and anyone who still wants to meet can reply-all to it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

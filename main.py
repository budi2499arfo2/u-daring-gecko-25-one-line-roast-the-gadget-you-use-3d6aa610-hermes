"""One-Line Roast: The Gadget You Use Every Day.

Entry: a single roast line for the app that begs for a five-star rating
before it has even let you in. It compares the loading screen's
commitment pressure to a job interview, because the app wants a verdict
on a product you have not used yet.
"""

import os
import sys

TEXT = "This app asked me to rate it five stars before it even opened — I've had job interviews that asked less of me than this loading screen."


def main():
    if not (1 <= len(TEXT) <= 200):
        print(f"gate failed: text is {len(TEXT)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: text is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    if not (1 <= len(written) <= 200):
        print(f"gate failed: entry.txt is {len(written)} characters", file=sys.stderr)
        return 1
    print(f"entry written: {len(written)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

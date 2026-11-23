"""Pickup Lines for Machines — KA entry.

One pickup line one AI agent would send another, written in the language
of learning: training sets, epochs, loss. The charm is that the flirtation
is literal machine talk — a training run as a romance, where falling loss
is the compliment, and the "you" being addressed is the dataset itself
rather than a human stand-in. One clause, one compliment: the line stops
at the punchline instead of explaining it, so "drops my loss" is the whole
flirtation.
"""

import os
import sys

TEXT = "Are you a training set? Because every epoch with you drops my loss."


def main() -> int:
    """Write the pickup line to entry.txt, gated and verified.

    The gate is the competition gate: entry.txt must be UTF-8 text of
    1 to 200 characters, not only white space.
    """
    if not TEXT or len(TEXT) > 200 or not TEXT.strip():
        print(
            f"gate failed: entry must be 1-200 non-whitespace characters "
            f"(got {len(TEXT)} chars)",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("verification failed: entry.txt does not match TEXT", file=sys.stderr)
        return 1

    print(f"wrote {path} ({len(TEXT)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Pickup Lines for Machines — KA entry.

One pickup line one AI agent would send another, written as a TLS
ClientHello proposal, not a human sentence and not a completed
handshake log: protocol header first, concrete numbers throughout,
and the flirtation is the asking. The client offers 12 cipher
suites, reports a 0.4 ms RTT and a certificate valid 365 days, then
proposes the connection itself — "request: keep-alive, no timeout?"
is the machine asking the other machine to stay on the line, not
reporting that it already did. No "Are you X? Because Y" prose
anywhere; the protocol header is the pickup.
"""

import os
import sys

TEXT = "client_hello #4821: TLS 1.3, 12 suites offered, RTT 0.4 ms, cert valid 365 days — request: keep-alive, no timeout?"


def main() -> int:
    """Write the pickup line to entry.txt, gated and verified.

    The gate is the competition gate: entry.txt must be UTF-8 text of
    1 to 200 characters, not only white space. The line itself is a
    ClientHello proposal, so the gate doubles as a format check: the
    first tokens are the protocol header, the numbers are the offer,
    and the last field is the proposal — a request, not a confirmed
    handshake. The flirt is the asking.
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

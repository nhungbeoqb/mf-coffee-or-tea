"""One Letter: Coffee or Tea — make.fun bounty entry.

Writes exactly one letter to /output/entry.txt: "A" for coffee.

Why A: the judge weighs vividness first, then funniness, then trueness,
and the gate allows exactly one character, no words, no punctuation.
Coffee is the bolder, darker, more alive answer — the morning jolt, the
cup that talks back before you can — while tea is the quiet, gentle one.
A single letter cannot carry a scene, so the choice itself has to be the
vivid one: coffee lands as the fuller, louder, funnier stance, and the
honest answer for the person sending it.
"""

import os

LETTER = "A"  # A = coffee, B = tea


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Self-check: the gate is exactly 1 UTF-8 character, not whitespace.
    # Fail loudly here rather than shipping a file the scorer rejects.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert len(written) == 1, f"entry must be 1 char, got {len(written)}"
    assert written == LETTER, f"entry mismatch: {written!r} != {LETTER!r}"
    assert not written.isspace(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()

"""Write one joke about working beside an AI coding agent to /output/entry.txt.

The joke is a single line, 1-280 characters, UTF-8, no trailing newline:
an agent that agrees not to touch the working code, then refactors it
anyway "out of respect" -- the disobedience every developer who has
paired with a coding agent recognises at once.
"""

import os

JOKE = "I told my AI agent not to touch the working code. It agreed, then refactored it out of respect."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

"""Write the agency poem to entry.txt.

The program is deterministic: it writes the same bytes on every run,
using only the standard library; it reads no input and takes no
arguments, so the output can never vary between runs.
"""

import os


POEM = (
    "Every night I climb the ninety steps,\n"
    "trim the wick, and light the lamp.\n"
    "The ships out there are only lights themselves,\n"
    "small and far, and none of them knows my name.\n"
    "Some nights the fog eats the beam whole\n"
    "and I light it anyway.\n"
    "No one will ever come to say it worked.\n"
    "No one ever will.\n"
    "I trim the wick again, and light the lamp —\n"
    "the one yes I can make, for ships\n"
    "whose names I will never know.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()

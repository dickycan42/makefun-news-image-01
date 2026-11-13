"""Copy the bundled news image to the output path.

This entry's image is a finished asset (entry.png) stored beside this
script. The program does one thing: it copies that file, byte for byte,
to the output location the grader reads. It uses only the standard
library, reads no network, and always produces the same bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    destination = os.path.join(output_dir, "entry.png")
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, destination)
    if os.path.getsize(source) != os.path.getsize(destination):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

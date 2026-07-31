#!/usr/bin/env python3
"""Point this mirror at a new vacuous release.

    python update.py 0.1.1

Rewrites the version and the pinned dependency, both of which have to match the
tag you are about to create.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PYPROJECT = Path(__file__).parent / "pyproject.toml"


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__.strip(), file=sys.stderr)
        return 2

    version = sys.argv[1].lstrip("v")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        print(f"expected a version like 0.1.1, got {version!r}", file=sys.stderr)
        return 2

    text = PYPROJECT.read_text(encoding="utf-8")
    text, n_version = re.subn(
        r'^version = "[^"]+"', f'version = "{version}"', text, count=1, flags=re.M
    )
    text, n_pin = re.subn(
        r'dependencies = \["vacuous==[^"]+"\]',
        f'dependencies = ["vacuous=={version}"]',
        text,
        count=1,
    )

    if not (n_version and n_pin):
        print("could not find both the version and the pin to update", file=sys.stderr)
        return 1

    PYPROJECT.write_text(text, encoding="utf-8")
    print(f"pinned to vacuous {version}")
    print(f"next: git commit -am 'Mirror vacuous {version}' && git tag v{version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

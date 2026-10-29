"""Check that README.md entries follow the list format.

Every tool entry must be a bullet under a category heading, with a link,
a one-line reason, and an install command in backticks. Entries repeated
across sections (like the replacements table) are fine -- only duplicates
inside one section are flagged, since that usually means a copy-paste slip.

Run from the repo root:  python3 tools/check_list.py
Exits 0 when the list is clean, 1 with the problems printed otherwise.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

# Matches one entry line, e.g.:
#   - [ripgrep](https://github.com/...) — reason here. `cargo install ripgrep`
ENTRY_RE = re.compile(
    r"^-\s+\[([^\]]+)\]\((https?://[^)]+)\)\s+—\s+(.+?)\s+`([^`]+)`\s*$"
)
HEADING_RE = re.compile(r"^##\s+(.+?)\s*$")

# Headings that are not tool categories (intro, meta sections).
NON_CATEGORY_HEADINGS = {"Contents", "My starter kit", "Contributing",
                          "Limitations", "License", "Author"}


@dataclass
class Entry:
    """One parsed tool entry from the README."""

    name: str
    url: str
    reason: str
    install: str
    section: str


def parse_entries(text: str) -> list[Entry]:
    """Return every well-formed entry, tagged with its section.

    Lines that look like entries but fail the pattern are skipped here;
    validate() reports them separately so a broken line can't hide.
    """
    entries: list[Entry] = []
    section = ""
    for line in text.splitlines():
        heading = HEADING_RE.match(line)
        if heading:
            section = heading.group(1)
            continue
        match = ENTRY_RE.match(line)
        if match and section not in NON_CATEGORY_HEADINGS:
            entries.append(Entry(
                name=match.group(1),
                url=match.group(2),
                reason=match.group(3),
                install=match.group(4),
                section=section,
            ))
    return entries


def validate(text: str) -> list[str]:
    """Return a list of problems found in the README text (empty = clean)."""
    problems: list[str] = []
    section = ""
    seen_in_section: set[tuple[str, str]] = set()
    for line in text.splitlines():
        heading = HEADING_RE.match(line)
        if heading:
            section = heading.group(1)
            continue
        if not line.startswith("- ["):
            continue
        if section in NON_CATEGORY_HEADINGS:
            continue
        match = ENTRY_RE.match(line)
        if not match:
            problems.append(f"Malformed entry line: {line}")
            continue
        name, url = match.group(1), match.group(2)
        key = (section, name.lower())
        if key in seen_in_section:
            problems.append(f"Duplicate entry '{name}' in section '{section}'")
        seen_in_section.add(key)
        if len(match.group(3).strip()) < 10:
            problems.append(f"Reason too short for '{name}'")
    entries = parse_entries(text)
    categories = {e.section for e in entries}
    if len(categories) < 4:
        problems.append(f"Only {len(categories)} categories found, expected >= 4")
    if len(entries) < 20:
        problems.append(f"Only {len(entries)} entries found, expected >= 20")
    return problems


def main(argv: list[str] | None = None) -> int:
    """Entry point: check README.md next to the repo root."""
    args = argv if argv is not None else sys.argv[1:]
    readme = Path(args[0]) if args else Path(__file__).resolve().parent.parent / "README.md"
    if not readme.is_file():
        print(f"error: README not found at {readme}", file=sys.stderr)
        return 2
    problems = validate(readme.read_text(encoding="utf-8"))
    if problems:
        print(f"{len(problems)} problem(s) in {readme}:", file=sys.stderr)
        for problem in problems:
            print(f"  - {problem}", file=sys.stderr)
        return 1
    entries = parse_entries(readme.read_text(encoding="utf-8"))
    print(f"OK: {len(entries)} entries across "
          f"{len({e.section for e in entries})} categories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

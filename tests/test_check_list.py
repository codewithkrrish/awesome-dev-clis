"""Tests for tools/check_list.py."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from check_list import parse_entries, validate

GOOD = """## Files and search

- [ripgrep](https://github.com/BurntSushi/ripgrep) — Search code fast, respects gitignore. `cargo install ripgrep`
- [fd](https://github.com/sharkdp/fd) — A simpler, faster find command. `cargo install fd-find`
"""

# 20 entries across 4 categories, so the size checks stay quiet.
BULK = "\n".join(
    f"## Category {i}\n\n"
    + "\n".join(
        f"- [tool{j}](https://example.com/{j}) — Does something genuinely useful here. `install tool{j}`"
        for j in range(i * 5, i * 5 + 5)
    )
    for i in range(4)
)


def test_parse_entries_tags_section() -> None:
    entries = parse_entries(GOOD)
    assert len(entries) == 2
    assert entries[0].name == "ripgrep"
    assert entries[0].section == "Files and search"
    assert entries[0].install == "cargo install ripgrep"


def test_validate_clean_list_passes() -> None:
    assert validate(BULK) == []


def test_validate_flags_malformed_entry() -> None:
    broken = BULK + "\n## Category 0\n\n- [noinstall](https://example.com/x) — Missing the install command.\n"
    problems = validate(broken)
    assert any("Malformed" in p for p in problems)


def test_validate_flags_duplicate_in_same_section() -> None:
    dup = BULK + "\n## Category 0\n\n- [tool0](https://example.com/0) — Repeated entry in the same section. `install tool0`\n"
    problems = validate(dup)
    assert any("Duplicate" in p for p in problems)


def test_validate_allows_repeat_across_sections() -> None:
    # The replacements section deliberately repeats tools from other sections.
    repeated = BULK + "\n## Replacements\n\n- [tool0](https://example.com/0) — Same tool, different section, fine. `install tool0`\n"
    assert validate(repeated) == []


def test_validate_flags_short_reason() -> None:
    short = BULK + "\n## Category 1\n\n- [tiny](https://example.com/t) — Tiny one. `install tiny`\n"
    # "Tiny one." is under 10 chars, so it must be flagged.
    assert any("too short" in p for p in validate(short))


def test_validate_flags_tiny_list() -> None:
    assert validate(GOOD)  # 2 entries, 1 category: fails the size checks

#!/usr/bin/env python3
"""Safely sync only approved GitHub Wiki tutorials.

Home.md and SQL-Performance.md are author-maintained and NEVER overwritten.
Existing Wiki pages remain intact. Only a marked block in _Sidebar.md is managed.
"""
from __future__ import annotations

import argparse
from pathlib import Path

MANAGED_PAGES = (
    "Database-Migration.md",
    "Data-Quality.md",
    "Python-Pandas.md",
    "Analytics-Engineering.md",
    "AI-Automation.md",
    "Enterprise-Reporting.md",
    "Reporting-Platforms.md",
    "Engineering-Roadmap.md",
)

START = "<!-- START DICURECK AUTOMATED TUTORIAL LINKS -->"
END = "<!-- END DICURECK AUTOMATED TUTORIAL LINKS -->"
NAVIGATION = """**Native Wiki Tutorials**

- [[Database Migration]]
- [[Data Quality]]
- [[Python Pandas]]
- [[Analytics Engineering]]
- [[AI Automation]]
- [[Enterprise Reporting]]
- [[Reporting Platforms]]
- [[Engineering Roadmap]]
"""


def sync(source: Path, target: Path) -> list[str]:
    if not source.is_dir() or not target.is_dir() or not (target / ".git").exists():
        raise ValueError("Source folder and a cloned native Wiki checkout are required")
    if not (target / "Home.md").is_file():
        raise ValueError("Existing Wiki homepage is missing: refusing to initialize or overwrite")
    if not (target / "SQL-Performance.md").is_file():
        raise ValueError("Author-maintained SQL Performance Wiki page missing: refusing update")
    missing = [name for name in MANAGED_PAGES if not (source / name).is_file()]
    if missing:
        raise ValueError("Missing approved tutorial pages: " + ", ".join(missing))
    sidebar = target / "_Sidebar.md"
    current_sidebar = sidebar.read_text(encoding="utf-8") if sidebar.exists() else ""
    if current_sidebar.count(START) != current_sidebar.count(END) or current_sidebar.count(START) > 1:
        raise ValueError("Unmatched or duplicated managed Sidebar markers: refusing sync")
    managed_block = START + "\n" + NAVIGATION + END
    if START in current_sidebar:
        left = current_sidebar.index(START)
        right = current_sidebar.index(END) + len(END)
        if left >= right:
            raise ValueError("Managed sidebar markers in the wrong order")
        next_sidebar = current_sidebar[:left] + managed_block + current_sidebar[right:]
    else:
        next_sidebar = current_sidebar.rstrip() + "\n\n---\n\n" + managed_block + "\n"

    # Validate every page before writing anything.
    contents = {}
    for name in MANAGED_PAGES:
        content = (source / name).read_text(encoding="utf-8")
        if not content.startswith("# ") or "https://github.com/Dicureck/" not in content:
            raise ValueError(f"Refusing invalid or ungrounded tutorial: {name}")
        contents[name] = content

    updated = []
    for name, content in contents.items():
        dest = target / name
        old = dest.read_text(encoding="utf-8") if dest.exists() else None
        if old != content:
            dest.write_text(content, encoding="utf-8")
            updated.append(name)
    if current_sidebar != next_sidebar:
        sidebar.write_text(next_sidebar, encoding="utf-8")
        updated.append("_Sidebar.md")
    return updated


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--target", required=True, type=Path)
    arguments = parser.parse_args()
    changed = sync(arguments.source, arguments.target)
    print("Managed pages updated:", ", ".join(changed) if changed else "(none)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build the English edition into one skill-pack zip.

Usage: python tools/build_pack.py [output.zip]

The zip has one top folder holding the pack README and the three skill
folders. Only text files go in, and every SKILL.md is checked for the
`name` and `description` frontmatter fields.
"""
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "skills" / "en"
TOP = "anthro-fantasy-film-kit"
TEXT_SUFFIXES = {".md", ".txt", ".py", ".json", ".yaml", ".yml"}


def check_skill(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise SystemExit(f"{path}: missing frontmatter")
    for field in ("name", "description"):
        if not re.search(rf"^{field}: \S", match.group(1), re.M):
            raise SystemExit(f"{path}: missing {field}")


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist" / f"{TOP}.zip"
    out.parent.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in SRC.rglob("*") if p.is_file())
    skills = [p for p in files if p.name == "SKILL.md"]
    if not skills:
        raise SystemExit("no SKILL.md found")
    for p in files:
        if p.suffix not in TEXT_SUFFIXES or p.is_symlink() or p.name.startswith("."):
            raise SystemExit(f"{p}: not allowed in the pack")
    for p in skills:
        check_skill(p)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in files:
            zf.write(p, f"{TOP}/{p.relative_to(SRC).as_posix()}")
    size = out.stat().st_size
    print(f"{out}: {len(skills)} skills, {len(files)} files, {size / 1024:.0f} KB")


if __name__ == "__main__":
    main()

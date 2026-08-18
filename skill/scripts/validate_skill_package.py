#!/usr/bin/env python3
"""Validate the basic structure of a Copilot Studio skill package.

Usage:
    python validate_skill_package.py <folder-or-zip> [--json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Iterable

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FORBIDDEN_NAMES = {"__pycache__", ".DS_Store", "Thumbs.db"}
FORBIDDEN_SUFFIXES = {".pyc", ".pyo", ".tmp", ".bak", "~"}


def parse_frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return {}, ["SKILL.md must start with YAML front matter delimited by ---."]

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, ["SKILL.md front matter is not closed with ---."]

    raw = text[4:end]
    data: dict[str, str] = {}
    current_key: str | None = None
    folded: list[str] = []

    def flush() -> None:
        nonlocal current_key, folded
        if current_key is not None and folded:
            data[current_key] = " ".join(part.strip() for part in folded if part.strip()).strip()
        current_key = None
        folded = []

    for line in raw.splitlines():
        if line.startswith(" ") and current_key:
            folded.append(line)
            continue
        flush()
        if ":" not in line:
            if line.strip():
                errors.append(f"Unsupported front matter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in {">", ">-", "|", "|-"}:
            current_key = key
            folded = []
        else:
            data[key] = value.strip('"\'')
    flush()
    return data, errors


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if path.is_file():
            yield path


def validate_folder(root: Path) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []

    skill = root / "SKILL.md"
    if not skill.is_file():
        errors.append("SKILL.md is missing at the package root.")
    else:
        try:
            text = skill.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append("SKILL.md is not valid UTF-8.")
            text = ""

        if text:
            frontmatter, fm_errors = parse_frontmatter(text)
            errors.extend(fm_errors)
            name = frontmatter.get("name", "").strip()
            description = frontmatter.get("description", "").strip()
            if not name:
                errors.append("Front matter field 'name' is missing or empty.")
            elif not NAME_RE.fullmatch(name):
                errors.append("Front matter 'name' must use lowercase letters, numbers, and hyphens only.")
            if not description:
                errors.append("Front matter field 'description' is missing or empty.")
            elif len(description) < 20:
                warnings.append("The description is very short; orchestration may be less accurate.")

    for path in iter_files(root):
        rel = path.relative_to(root)
        if any(part in FORBIDDEN_NAMES for part in rel.parts):
            errors.append(f"Forbidden generated file or folder: {rel.as_posix()}")
        if path.suffix in FORBIDDEN_SUFFIXES or path.name.endswith("~"):
            errors.append(f"Forbidden temporary file: {rel.as_posix()}")
        try:
            if path.suffix.lower() in {".md", ".txt", ".py", ".json", ".yaml", ".yml"}:
                path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"Text file is not valid UTF-8: {rel.as_posix()}")

    nested_skills = [p.relative_to(root).as_posix() for p in root.rglob("SKILL.md") if p != skill]
    if nested_skills:
        warnings.append("Nested SKILL.md files found: " + ", ".join(nested_skills))

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "file_count": sum(1 for _ in iter_files(root)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    target = args.path.resolve()
    if not target.exists():
        result = {"valid": False, "errors": [f"Path not found: {target}"], "warnings": [], "file_count": 0}
    elif target.is_dir():
        result = validate_folder(target)
    elif target.suffix.lower() == ".zip":
        with tempfile.TemporaryDirectory(prefix="skill-validate-") as tmp:
            tmp_path = Path(tmp)
            try:
                with zipfile.ZipFile(target) as archive:
                    bad = archive.testzip()
                    if bad:
                        result = {"valid": False, "errors": [f"Corrupted ZIP entry: {bad}"], "warnings": [], "file_count": 0}
                    else:
                        archive.extractall(tmp_path)
                        roots = [p for p in tmp_path.iterdir()]
                        if not (tmp_path / "SKILL.md").exists() and len(roots) == 1 and roots[0].is_dir():
                            result = validate_folder(roots[0])
                            result["valid"] = False
                            result["errors"].insert(0, "The ZIP contains a wrapper folder. SKILL.md must be at ZIP root.")
                        else:
                            result = validate_folder(tmp_path)
            except zipfile.BadZipFile:
                result = {"valid": False, "errors": ["The file is not a valid ZIP archive."], "warnings": [], "file_count": 0}
    else:
        result = {"valid": False, "errors": ["Provide a skill folder or a ZIP file."], "warnings": [], "file_count": 0}

    if args.as_json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print("VALID" if result["valid"] else "INVALID")
        print(f"Files checked: {result['file_count']}")
        for warning in result["warnings"]:
            print(f"WARNING: {warning}")
        for error in result["errors"]:
            print(f"ERROR: {error}")

    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())

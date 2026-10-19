#!/usr/bin/env python3
"""Validate and package the portable ELI5 Agent Plugin."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


REQUIRED_MANIFEST_KEYS = {"$schema", "name", "version", "description"}


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    manifest_path = root / "plugin.json"
    skill_path = root / "skills" / "eli5-learning" / "SKILL.md"

    if not manifest_path.is_file():
        errors.append("missing root plugin.json")
    else:
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"invalid plugin.json: {exc}")
        else:
            missing = REQUIRED_MANIFEST_KEYS - manifest.keys()
            if missing:
                errors.append("plugin.json missing: " + ", ".join(sorted(missing)))
            if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
                errors.append("plugin.json must declare the Agent Plugins 1.0.0 schema")
            if not isinstance(manifest.get("name"), str) or not manifest["name"]:
                errors.append("plugin.json name must be a non-empty string")

    if not skill_path.is_file():
        errors.append("missing skills/eli5-learning/SKILL.md")
    else:
        try:
            lines = skill_path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            errors.append(f"cannot read SKILL.md: {exc}")
        else:
            if len(lines) < 4 or lines[0].strip() != "---":
                errors.append("SKILL.md must start with YAML front matter")
            elif "---" not in lines[1:]:
                errors.append("SKILL.md YAML front matter is not closed")
            else:
                end = lines[1:].index("---") + 1
                header = "\n".join(lines[1:end])
                if "name:" not in header or "description:" not in header:
                    errors.append("SKILL.md front matter needs name and description")

    return errors


def package(root: Path, output: Path) -> None:
    errors = validate(root)
    if errors:
        raise SystemExit("Validation failed:\n- " + "\n- ".join(errors))

    output.parent.mkdir(parents=True, exist_ok=True)
    excluded_parts = {".git", "__pycache__", "dist"}
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            if not path.is_file() or any(part in excluded_parts for part in path.parts):
                continue
            archive.write(path, path.relative_to(root).as_posix())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "package"))
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    errors = validate(root)
    if args.command == "validate":
        if errors:
            print("Validation failed:")
            print("\n".join(f"- {error}" for error in errors))
            return 1
        print(f"Validated {root}")
        return 0

    output = args.output or root / "dist" / "eli5-learning-companion.zip"
    package(root, output.resolve())
    print(f"Validated and packaged {output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

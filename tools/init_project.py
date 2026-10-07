from __future__ import annotations

import argparse
from pathlib import Path


TEXT_EXTENSIONS = {
    ".md", ".yaml", ".yml", ".toml", ".py", ".sh", ".txt", ".json", ".csv"
}


def replace_in_file(path: Path, replacements: dict[str, str]) -> None:
    if path.suffix.lower() not in TEXT_EXTENSIONS and path.name not in {"Makefile", ".gitignore"}:
        return
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return
    new_text = text
    for old, new in replacements.items():
        new_text = new_text.replace(old, new)
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Human-readable project name")
    parser.add_argument("--slug", required=True, help="Repository/project slug")
    parser.add_argument("--package", required=True, help="Python package name")
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    replacements = {
        "PROJECT_NAME": args.name,
        "project_slug": args.slug,
        "project-name": args.slug.replace("_", "-"),
        "project_name": args.package,
    }

    for path in root.rglob("*"):
        if path.is_file() and ".git" not in path.parts:
            replace_in_file(path, replacements)

    src_old = root / "src" / "project_name"
    src_new = root / "src" / args.package
    if src_old.exists() and src_old != src_new:
        src_old.rename(src_new)

    print(f"Initialized project: {args.name}")
    print(f"Slug: {args.slug}")
    print(f"Python package: {args.package}")
    print("Next: edit PROJECT.yaml, docs/project_state.md, docs/datasets.md, and docs/methodology.md.")


if __name__ == "__main__":
    main()

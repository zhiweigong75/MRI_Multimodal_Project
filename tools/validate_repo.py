from __future__ import annotations

from pathlib import Path
import csv
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "PROJECT.yaml",
    "AGENTS.md",
    ".gitignore",
    "docs/project_state.md",
    "docs/methodology.md",
    "docs/datasets.md",
    "experiments/registry.csv",
    ".agents/skills/research-experiment/SKILL.md",
    ".agents/skills/research-figure/SKILL.md",
    ".agents/skills/research-presentation/SKILL.md",
]

FORBIDDEN_TRACK_CANDIDATES = [
    ".venv",
    "venv",
    "__pycache__",
]


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"Missing required file: {rel}")

    registry = ROOT / "experiments/registry.csv"
    if registry.exists():
        with registry.open("r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            header = next(reader, [])
        if "experiment_id" not in header or "status" not in header:
            errors.append("Experiment registry header is invalid.")

    for name in FORBIDDEN_TRACK_CANDIDATES:
        if (ROOT / name).exists():
            errors.append(f"Local/generated directory exists in repository root: {name}")

    if errors:
        print("Repository validation FAILED")
        for e in errors:
            print(f"- {e}")
        return 1

    print("Repository validation PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

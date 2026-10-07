from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()

    config_path = Path(args.config)
    with config_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    raise NotImplementedError(
        "Template entrypoint only. Implement project-specific training logic in src/ "
        "and keep this script as a thin CLI wrapper."
    )


if __name__ == "__main__":
    main()

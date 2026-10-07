#!/usr/bin/env bash
#SBATCH --job-name=PROJECT_E000
#SBATCH --partition=TODO
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=04:00:00
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err

set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Customize for the project:
# module purge
# module load <PROJECT_MODULE>
# source .venv/bin/activate

CONFIG="${1:-configs/experiment/E000_template.yaml}"

echo "Project root: $PROJECT_ROOT"
echo "Config: $CONFIG"
echo "Git commit: $(git rev-parse HEAD)"
echo "Slurm job: ${SLURM_JOB_ID:-NA}"

python scripts/train/train.py --config "$CONFIG"

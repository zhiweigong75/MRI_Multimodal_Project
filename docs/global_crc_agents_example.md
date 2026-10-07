# Example `~/.codex/AGENTS.md` for CRC

This file is NOT automatically installed by the template. Copy/adapt it manually if desired.

```markdown
# Global Research Environment Rules

This machine is a research HPC environment.

- Do not run long or GPU-intensive training on login nodes.
- Use Slurm for compute workloads.
- Never modify source datasets unless explicitly instructed.
- Never recursively delete research data without explicit confirmation.
- Never commit raw datasets, medical data, PHI, credentials, checkpoints,
  large experiment outputs, virtual environments, or caches.
- Prefer project-local configs over hard-coded absolute paths.
```

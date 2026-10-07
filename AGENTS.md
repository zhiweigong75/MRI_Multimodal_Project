# Research Repository Instructions

This repository contains reproducible academic research code.

## Source of truth

The Git repository, tracked configs, manifests, experiment registry, and tracked documentation are authoritative.

Do not rely on prior chat history when repository evidence is available.

## Research integrity

- Never silently modify dataset splits, patient IDs, labels, evaluation cohorts, or primary metrics.
- Never use target test labels for training, tuning, early stopping, model selection, or prompt construction unless the experiment explicitly studies that setting.
- Do not invent experimental results, metrics, architecture components, clinical variables, or dataset properties.
- Preserve patient-level separation when the task requires it.

## Repository organization

- Reusable code belongs in `src/`.
- Experiment differences should normally be config-driven, not implemented through duplicated training scripts.
- Formal experiment configs belong in `configs/experiment/`.
- Slurm launchers belong in `slurm/`.
- Do not create ad-hoc scripts in the repository root.

## CRC / HPC

- Long-running or GPU-intensive work must use Slurm.
- Do not run full training jobs on login nodes.
- Raw datasets, PHI, credentials, checkpoints, caches, large outputs, virtual environments, and Slurm `.out/.err` logs must not be committed.

## Workflow routing

- Formal experiment → use `research-experiment`.
- Framework / architecture / pipeline figure → use `research-figure`.
- Advisor / lab / conference deck → use `research-presentation`.
- Update the canonical current state → use `project-state`.
- Repository-wide structural/evidence audit → use `repo-audit`.
- Major multi-stage changes → write an execution plan following `.agent/PLANS.md`.

## Verification

Before handing off code changes:

1. run relevant tests;
2. run data-integrity checks when applicable;
3. run a smoke test before a full experiment;
4. inspect `git diff`;
5. summarize changed files, assumptions, and remaining risks.

Do not commit automatically unless explicitly requested.

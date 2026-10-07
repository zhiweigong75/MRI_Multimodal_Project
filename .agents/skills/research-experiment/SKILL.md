# Skill: research-experiment

Use this workflow for every formal experiment.

## Required order

1. **Inspect**
   - Read `PROJECT.yaml`.
   - Read `docs/project_state.md`.
   - Read relevant methodology, configs, code, and prior experiment summaries.
   - Identify protected splits and evaluation rules.

2. **Specify**
   Create/update `experiments/specs/E###_<name>.md` with:
   - research question
   - hypothesis
   - baseline/comparator
   - one intended change
   - frozen controls
   - primary endpoint
   - secondary endpoints
   - success/failure interpretation
   - leakage risks

3. **Configure**
   Create `configs/experiment/E###_<name>.yaml`.
   Prefer config changes over duplicated Python scripts.

4. **Implement**
   Reuse existing abstractions.
   Keep reusable logic in `src/`.

5. **Validate**
   Run:
   - unit tests
   - split/data-integrity checks
   - smoke test
   - shape/loss/output checks

6. **Review**
   Show:
   - `git status`
   - `git diff`
   - changed files
   - scientific assumptions changed or preserved

7. **Formal run**
   Prefer a committed code state.
   Submit via Slurm.
   Do not launch a full job automatically unless explicitly requested.

8. **Provenance**
   Produce a manifest with:
   - experiment ID
   - Git commit
   - config
   - seed
   - Slurm job ID
   - dataset/split identity
   - domains
   - timestamps

9. **Summarize**
   Create `reports/summaries/E###.md`.
   Update `experiments/registry.csv`.

10. **State update**
    Update `docs/project_state.md`.

## Non-negotiable rules

- Never silently change patient splits.
- Never silently change evaluation cohorts or primary metrics.
- Never use held-out target labels improperly.
- Never rename an existing formal experiment ID to represent a different experiment.

# AI-Native Research Project Template v1

A reusable repository template for reproducible academic ML / medical-AI research on HPC systems such as Pitt CRC.

The repository is designed around five layers:

1. **Scientific reasoning** — research questions, hypotheses, decisions.
2. **Engineering** — reusable code, configs, tests, Git history.
3. **Experiment execution** — Slurm jobs, manifests, outputs, provenance.
4. **Evidence management** — experiment summaries, project state, source manifests.
5. **Research communication** — publication-style framework/pipeline figures, advisor/lab/conference slides, and speaker notes.

## Core rule

The Git repository is the authoritative project state. Chat history is not.

If a prior conversation conflicts with tracked configs, manifests, source code, or documentation, use the repository as the source of truth.

## Quick start

After copying/cloning this template into a new project:

```bash
python tools/init_project.py \
  --name "My Research Project" \
  --slug my_research_project \
  --package my_research_project

git status
git add .
git commit -m "chore: initialize project from research template"
```

Then:

1. Fill `PROJECT.yaml`.
2. Configure CRC paths in `configs/local/paths.yaml` using `paths.example.yaml`.
3. Update `docs/project_state.md`, `docs/datasets.md`, and `docs/methodology.md`.
4. Register baseline experiments starting from `E001`.
5. Use `.agents/skills/research-experiment/SKILL.md` for formal experiments.
6. Use `.agents/skills/research-figure/SKILL.md` for framework/pipeline figures.
7. Use `.agents/skills/research-presentation/SKILL.md` for advisor/lab/conference decks.

See `DEPLOYMENT.md` for the full deployment and daily-use workflow.

# Deployment and Daily Workflow

## A. One-time: make this your template repository

On CRC:

```bash
cd /ix1/swu/zhiwei
mkdir research-project-template
cd research-project-template
# Copy the contents of this template here.
git init -b main
git add .
git commit -m "chore: initialize AI-native research project template"
```

Create a private GitHub repository and push it using your normal Git/GitHub workflow.

Keep the template repository generic. Do not put project data, institutional secrets, PHI, credentials, checkpoints, or real experiment outputs into the template.

---

## B. Start a new project

Recommended CRC location:

```bash
cd /ix1/swu/zhiwei
```

Copy or clone the template into the new project directory, then initialize the project metadata:

```bash
python tools/init_project.py \
  --name "Project Display Name" \
  --slug project_slug \
  --package project_slug
```

If you copied an existing Git template clone and want a completely independent history:

```bash
rm -rf .git
git init -b main
git add .
git commit -m "chore: initialize project from research template"
```

Create a new private GitHub repository for the project and push.

---

## C. Configure the CRC environment

Never commit `.venv/`.

Example:

```bash
module purge
module load <PROJECT_MODULE>

python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
```

Project-specific absolute paths belong in:

```text
configs/local/paths.yaml
```

Create it from:

```bash
cp configs/local/paths.example.yaml configs/local/paths.yaml
```

`paths.yaml` is ignored by Git.

---

## D. Daily startup

```bash
cd /ix1/swu/zhiwei/PROJECT_NAME

git pull --ff-only
git status

module purge
module load <PROJECT_MODULE>
source .venv/bin/activate
```

Open the repository through VS Code Remote SSH or your preferred Codex remote workflow.

---

## E. Scientific workflow

### 1. Reason in ChatGPT first

Use ChatGPT for:

- problem formulation
- methodology
- experimental controls
- ablations
- interpretation
- paper logic
- what to test next

End the discussion with a compact experiment specification.

### 2. Hand the specification to Codex

Ask Codex to use the `research-experiment` workflow.

Recommended first phase:

```text
Use the research-experiment workflow.

Inspect the repository first.

Before changing files, report:
1. relevant files
2. proposed implementation
3. scientific risks
4. leakage risks
5. tests required

Do not modify frozen dataset splits.
Do not launch a full Slurm job.
```

Only after reviewing the plan should implementation proceed.

### 3. Test before formal runs

Order:

```text
unit tests
→ data/split integrity checks
→ smoke test
→ inspect git diff
→ commit
→ full Slurm run
```

A formal experiment should normally start from a committed code state.

### 4. Register the experiment

Every formal experiment receives an immutable ID:

```text
E001, E002, E003, ...
```

Create:

```text
experiments/specs/E###_<name>.md
configs/experiment/E###_<name>.yaml
```

Update:

```text
experiments/registry.csv
```

### 5. Save provenance

Every formal run should produce a manifest containing at least:

- experiment ID
- Git commit
- config path
- seed
- Slurm job ID
- dataset/split identity
- source/target domain when applicable
- timestamps

### 6. Summarize completed experiments

Create:

```text
reports/summaries/E###.md
```

This is the preferred input for later ChatGPT interpretation and slide generation. Avoid using thousands of lines of raw terminal logs as the primary research record.

---

## F. Framework / pipeline / architecture figures

Use the `research-figure` skill.

The workflow is:

```text
repository evidence
→ source manifest
→ scientific specification
→ scientific invariants
→ visual prompt
→ generation
→ validation
```

A formal figure folder should look like:

```text
reports/figures/F001_method_architecture/
├── scientific_spec.md
├── source_manifest.yaml
├── prompt.md
├── figure.png
└── validation.md
```

Scientific truth and visual design must be kept separate.

The image prompt must never invent:

- model components
- connections
- datasets
- clinical variables
- metrics
- labels
- results

---

## G. Presentations

Use the `research-presentation` skill.

A formal deck folder should look like:

```text
reports/presentations/YYYY-MM-DD_topic/
├── presentation_brief.md
├── source_manifest.yaml
├── deck_outline.md
├── speaker_notes.md
├── slides.pptx
├── build_manifest.json
├── previews/
└── preview_validation.json
```

### Advisor update narrative

```text
Question
→ experiment
→ result
→ interpretation
→ uncertainty
→ decision / next step
```

### Lab meeting narrative

```text
Problem
→ motivation
→ research question
→ dataset
→ method
→ experiment design
→ results
→ interpretation
→ limitations
→ next experiments
```

### Conference narrative

```text
Problem
→ gap
→ core insight
→ method
→ key evidence
→ contribution
→ why it matters
```

Detailed methodology belongs in the appendix when possible.

---

## H. Git discipline

Prefer meaningful commits:

```text
feat: add PID multimodal fusion
exp: add E021 modality-specific CORAL configuration
test: add patient split integrity checks
fix: prevent target labels from entering training
docs: update project state after E021
```

Avoid:

```text
update
fix
new
final
final2
```

Before a formal experiment:

```bash
git status
```

Prefer a clean working tree.

---

## I. End-of-session handoff

Before stopping work:

1. Update `docs/project_state.md`.
2. Update `experiments/registry.csv` if experiment status changed.
3. Save result summaries for completed experiments.
4. Commit meaningful repository changes.
5. Push to GitHub.
6. Record unresolved risks / next steps.

A new ChatGPT or Codex session should be able to resume from the repository without requiring the old chat transcript.

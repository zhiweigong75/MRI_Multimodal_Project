# Skill: research-presentation

Use this workflow for advisor updates, lab meetings, project reviews, and conference presentations.

## Step 1: Ground the deck

Read:
- `PROJECT.yaml`
- `docs/project_state.md`
- `experiments/registry.csv`
- completed `reports/summaries/`
- relevant methodology and figure source manifests

Use completed/saved evidence only unless a slide explicitly labels work as ongoing or planned.

## Step 2: Create presentation folder

`reports/presentations/YYYY-MM-DD_<topic>/`

Create:
- `presentation_brief.md`
- `source_manifest.yaml`
- `deck_outline.md`
- `speaker_notes.md`

Do not build the final PPTX before the evidence and narrative are coherent.

## Step 3: Choose narrative

### Advisor
Question → experiment → result → interpretation → uncertainty → decision/next step

### Lab meeting
Problem → motivation → question → dataset → method → experiment design → results → interpretation → limitations → next experiments

### Conference
Problem → gap → core insight → method → key evidence → contribution → why it matters

## Step 4: Slide rules

Each result slide should answer:
1. What question were we testing?
2. What changed?
3. What happened?
4. What can we conclude?
5. What can we not conclude?

Prefer question-driven slide titles.

Detailed methodology belongs in appendix slides when possible.

## Step 5: Visual style

Use `ai_workflows/style/presentation_style.md`.

Default:
- 16:9
- white or very light background
- generous whitespace
- restrained academic palette
- large readable type
- few elements per slide
- editable charts/tables where possible
- minimal decoration

## Step 6: Notes

Maintain a standalone `speaker_notes.md`.
Speaker notes should be natural spoken explanations, not paragraphs copied from the slide.

## Step 7: Build provenance

If a PPTX is produced, also save:
- `build_manifest.json`
- preview images/contact sheet
- `preview_validation.json`

## Step 8: Validate

Check:
- numbers trace to sources
- slide titles match the evidence
- no unsupported significance language
- no invented results
- no accidental leakage of private paths/PHI
- notes match slide order
- appendix contains necessary methodological detail

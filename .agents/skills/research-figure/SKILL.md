# Skill: research-figure

Use this workflow for formal framework, architecture, or pipeline figures.

## Objective

Generate a figure specification that is grounded in repository evidence and separates scientific truth from visual design.

## Workflow

1. Read:
   - `PROJECT.yaml`
   - `docs/methodology.md`
   - `docs/project_state.md`
   - relevant code
   - relevant configs
   - relevant completed experiment summaries

2. Create a figure folder:
   `reports/figures/F###_<name>/`

3. Create `source_manifest.yaml`.
   List the exact files/configs/experiments that support the figure.

4. Create `scientific_spec.md` containing:
   - purpose
   - inputs
   - outputs
   - modules
   - data flow
   - training-only components
   - inference-only components
   - exact labels
   - scientific invariants
   - forbidden arrows/connections
   - forbidden claims

5. Create `prompt.md` using:
   `ai_workflows/templates/figure_prompt_template.md`

6. Keep scientific and visual constraints separate.

7. Generation style defaults:
   - 16:9 landscape when used for research slides
   - clean white canvas
   - generous whitespace
   - journal-methods aesthetic
   - restrained navy / teal palette
   - optional small amber/coral accent
   - flat vector-like shapes
   - thin precise arrows
   - large readable sans-serif text
   - minimal decoration
   - no 3D
   - no fictional components

8. After generation, create `validation.md`.
   Verify:
   - every module exists in the evidence
   - every arrow is scientifically valid
   - labels are correct
   - training-only information is not shown as inference input
   - no metric/result was invented
   - no unsupported clinical variable/data source was invented

## Principle

Visual quality never overrides architectural truth.

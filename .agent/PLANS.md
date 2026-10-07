# Execution Plans

Use an execution plan for changes that are large, multi-stage, high-risk, or likely to touch multiple scientific assumptions.

A plan should contain:

## Goal
What outcome is being requested?

## Scientific invariants
What must not change?

## Evidence inspected
Which repository files establish the current implementation?

## Proposed changes
Which files will change, and why?

## Risks
Include:
- data leakage
- split drift
- label misuse
- metric changes
- backward incompatibility
- reproducibility risks

## Validation
Specify:
- unit tests
- data-integrity checks
- smoke test
- expected outputs

## Rollback
How can the previous state be recovered?

Do not treat a plan as permission to silently change protected scientific assumptions.

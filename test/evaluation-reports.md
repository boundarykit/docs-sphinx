---
title: "Evaluation reports"
---

# Evaluation reports

Evaluation reports — attach the evaluator revision to the exported report.

## Test contract

Attach the evaluator revision to the exported report.

## Fixture fields

```json
{
  "case": "evaluation-reports",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Attach the evaluator revision to the exported report."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Evaluation reports**. Compare its organization and revision with the values in the fixture before interpreting the result.

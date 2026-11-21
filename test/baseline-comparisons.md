---
title: "Verification: Baseline comparisons"
---

# Verification: Baseline comparisons

Baseline comparisons — separate intentional policy changes from fixture churn.

## Test contract

Separate intentional policy changes from fixture churn.

## Fixture fields

```json
{
  "case": "baseline-comparisons",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Separate intentional policy changes from fixture churn."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Baseline comparisons**. Compare its organization and revision with the values in the fixture before interpreting the result.

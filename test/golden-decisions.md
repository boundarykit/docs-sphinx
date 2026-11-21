---
title: "Golden decisions"
description: "Use golden decisions in a scoped workspace and verify the result with evaluations records."
---

# Golden decisions

Golden decisions — compare the matched rule as well as the final effect.

## Test contract

Compare the matched rule as well as the final effect.

## Fixture fields

```json
{
  "case": "golden-decisions",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Compare the matched rule as well as the final effect."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Golden decisions**. Compare its organization and revision with the values in the fixture before interpreting the result.

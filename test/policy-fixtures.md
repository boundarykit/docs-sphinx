---
title: "Policy fixtures"
description: "Use policy fixtures in a scoped workspace and verify the result with evaluations records."
---

# Policy fixtures

Policy fixtures — remove unstable timestamps from the expected output.

## Test contract

Remove unstable timestamps from the expected output.

## Fixture fields

```json
{
  "case": "policy-fixtures",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Remove unstable timestamps from the expected output."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Policy fixtures**. Compare its organization and revision with the values in the fixture before interpreting the result.

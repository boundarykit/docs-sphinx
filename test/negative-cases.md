---
title: "Negative cases"
description: "Use negative cases in a scoped workspace and verify the result with evaluations records."
---

# Negative cases

Negative cases — exercise an explicitly denied capability with a valid identity.

## Test contract

Exercise an explicitly denied capability with a valid identity.

## Fixture fields

```json
{
  "case": "negative-cases",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Exercise an explicitly denied capability with a valid identity."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Negative cases**. Compare its organization and revision with the values in the fixture before interpreting the result.

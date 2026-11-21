---
title: "Nested rule tests"
description: "Use nested rule tests in a scoped workspace and verify the result with evaluations records."
---

# Nested rule tests

Nested rule tests — include a denied leaf underneath an allowed parent.

## Test contract

Include a denied leaf underneath an allowed parent.

## Fixture fields

```json
{
  "case": "nested-rule-tests",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Include a denied leaf underneath an allowed parent."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Nested rule tests**. Compare its organization and revision with the values in the fixture before interpreting the result.

---
title: "Verification: Sandbox isolation tests"
---

# Verification: Sandbox isolation tests

Sandbox isolation tests — try reading a resource from a sibling sandbox.

## Test contract

Try reading a resource from a sibling sandbox.

## Fixture fields

```json
{
  "case": "sandbox-isolation-tests",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Try reading a resource from a sibling sandbox."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Sandbox isolation tests**. Compare its organization and revision with the values in the fixture before interpreting the result.

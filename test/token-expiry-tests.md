---
title: "Verification: Token expiry tests"
---

# Verification: Token expiry tests

Token expiry tests — exercise timestamps on both sides of the expiry boundary.

## Test contract

Exercise timestamps on both sides of the expiry boundary.

## Fixture fields

```json
{
  "case": "token-expiry-tests",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Exercise timestamps on both sides of the expiry boundary."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Token expiry tests**. Compare its organization and revision with the values in the fixture before interpreting the result.

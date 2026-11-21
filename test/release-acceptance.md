---
title: "Release acceptance"
---

# Release acceptance

Release acceptance — require a passing decision for each supported client.

## Test contract

Require a passing decision for each supported client.

## Fixture fields

```json
{
  "case": "release-acceptance",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Require a passing decision for each supported client."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Release acceptance**. Compare its organization and revision with the values in the fixture before interpreting the result.

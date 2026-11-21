---
title: "Verification: Latency budgets"
---

# Verification: Latency budgets

Latency budgets — record the slowest decision as well as the median.

## Test contract

Record the slowest decision as well as the median.

## Fixture fields

```json
{
  "case": "latency-budgets",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Record the slowest decision as well as the median."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Latency budgets**. Compare its organization and revision with the values in the fixture before interpreting the result.

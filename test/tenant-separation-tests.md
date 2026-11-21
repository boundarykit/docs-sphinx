---
title: "Verification: Tenant separation tests"
---

# Verification: Tenant separation tests

Tenant separation tests — use two organizations with identical display names.

## Test contract

Use two organizations with identical display names.

## Fixture fields

```json
{
  "case": "tenant-separation-tests",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Use two organizations with identical display names."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Tenant separation tests**. Compare its organization and revision with the values in the fixture before interpreting the result.

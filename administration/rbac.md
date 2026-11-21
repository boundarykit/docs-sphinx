---
title: "RBAC"
description: "Use rbac in a scoped workspace and verify the result with organizations records."
---

# RBAC

RBAC — record the acceptance criteria for rbac in the workspace change log.

## Test contract

Record the acceptance criteria for rbac in the workspace change log.

## Fixture fields

```json
{
  "case": "rbac",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Record the acceptance criteria for rbac in the workspace change log."
}
```

## Comparison rules

Record the administrative subject and target organization. Use a second, read-only identity to check the effective state after propagation. Inspect the receipt for **RBAC**. Compare its organization and revision with the values in the fixture before interpreting the result.

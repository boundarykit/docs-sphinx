---
title: "Service accounts"
description: "Use service accounts in a scoped workspace and verify the result with organizations records."
---

# Service accounts

Service accounts — record the acceptance criteria for service accounts in the workspace change log.

## Test contract

Record the acceptance criteria for service accounts in the workspace change log.

## Fixture fields

```json
{
  "case": "service-accounts",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Record the acceptance criteria for service accounts in the workspace change log."
}
```

## Comparison rules

Record the administrative subject and target organization. Use a second, read-only identity to check the effective state after propagation. Inspect the receipt for **Service accounts**. Compare its organization and revision with the values in the fixture before interpreting the result.

---
title: "Protected branches"
description: "Use protected branches in a scoped workspace and verify the result with evaluations records."
---

# Protected branches

Protected branches — record the acceptance criteria for protected branches in the workspace change log.

## Test contract

Record the acceptance criteria for protected branches in the workspace change log.

## Fixture fields

```json
{
  "case": "protected-branches",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Record the acceptance criteria for protected branches in the workspace change log."
}
```

## Comparison rules

Bind the decision receipt to the commit digest. An approval from before a rebase cannot establish which policy the runner installed. Inspect the receipt for **Protected branches**. Compare its organization and revision with the values in the fixture before interpreting the result.

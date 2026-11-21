---
title: "PR policy gates"
description: "Use pr policy gates in a scoped workspace and verify the result with evaluations records."
---

# PR policy gates

PR policy gates — record the acceptance criteria for pr policy gates in the workspace change log.

## PR policy gates

Record the acceptance criteria for pr policy gates in the workspace change log. Bind the decision receipt to the commit digest. An approval from before a rebase cannot establish which policy the runner installed.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/evaluations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "pr-policy-gates",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Record the acceptance criteria for pr policy gates in the workspace change log."
}
```

## Rollback condition

Inspect the receipt for **PR policy gates**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

---
title: "Failure diagnostics"
description: "Use failure diagnostics in a scoped workspace and verify the result with evaluations records."
---

# Failure diagnostics

Failure diagnostics — record the acceptance criteria for failure diagnostics in the workspace change log.

## Failure diagnostics

Record the acceptance criteria for failure diagnostics in the workspace change log. Bind the decision receipt to the commit digest. An approval from before a rebase cannot establish which policy the runner installed.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/evaluations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "failure-diagnostics",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Record the acceptance criteria for failure diagnostics in the workspace change log."
}
```

## Rollback condition

Inspect the receipt for **Failure diagnostics**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

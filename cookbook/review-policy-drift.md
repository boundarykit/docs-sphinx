---
title: "Review policy drift"
description: "Use review policy drift in a scoped workspace and verify the result with audits records."
---

# Review policy drift

Review policy drift — compare the live revision with the committed manifest.

## Review policy drift

Compare the live revision with the committed manifest. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/audits" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "review-policy-drift",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Compare the live revision with the committed manifest."
}
```

## Rollback condition

Inspect the receipt for **Review policy drift**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

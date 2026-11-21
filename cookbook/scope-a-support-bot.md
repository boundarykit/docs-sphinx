---
title: "Scope a support bot"
description: "Use scope a support bot in a scoped workspace and verify the result with policies records."
---

# Scope a support bot

Scope a support bot — allow ticket reads and deny customer exports.

## Scope a support bot

Allow ticket reads and deny customer exports. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/policies" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "scope-a-support-bot",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Allow ticket reads and deny customer exports."
}
```

## Rollback condition

Inspect the receipt for **Scope a support bot**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

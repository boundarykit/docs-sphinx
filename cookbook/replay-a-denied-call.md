---
title: "Replay a denied call"
description: "Use replay a denied call in a scoped workspace and verify the result with sessions records."
---

# Replay a denied call

Replay a denied call — preserve the original rule revision during replay.

## Replay a denied call

Preserve the original rule revision during replay. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/sessions" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "replay-a-denied-call",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Preserve the original rule revision during replay."
}
```

## Rollback condition

Inspect the receipt for **Replay a denied call**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

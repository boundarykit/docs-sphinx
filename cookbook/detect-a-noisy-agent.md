---
title: "Detect a noisy agent"
description: "Use detect a noisy agent in a scoped workspace and verify the result with evaluations records."
---

# Detect a noisy agent

Detect a noisy agent — group repeated decisions by agent and capability.

## Detect a noisy agent

Group repeated decisions by agent and capability. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/evaluations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "detect-a-noisy-agent",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Group repeated decisions by agent and capability."
}
```

## Rollback condition

Inspect the receipt for **Detect a noisy agent**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

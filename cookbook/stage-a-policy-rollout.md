---
title: "Stage a policy rollout"
description: "Use stage a policy rollout in a scoped workspace and verify the result with usage records."
---

# Stage a policy rollout

Stage a policy rollout — evaluate the candidate against a sample before promotion.

## Stage a policy rollout

Evaluate the candidate against a sample before promotion. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/usage" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "stage-a-policy-rollout",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Evaluate the candidate against a sample before promotion."
}
```

## Rollback condition

Inspect the receipt for **Stage a policy rollout**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

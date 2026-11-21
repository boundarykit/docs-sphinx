---
title: "Test nested rules"
description: "Use test nested rules in a scoped workspace and verify the result with webhooks records."
---

# Test nested rules

Test nested rules — evaluate a denied child under an allowed parent.

## Test nested rules

Evaluate a denied child under an allowed parent. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/webhooks" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "test-nested-rules",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Evaluate a denied child under an allowed parent."
}
```

## Rollback condition

Inspect the receipt for **Test nested rules**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

---
title: "Rotate an API key"
description: "Use rotate an api key in a scoped workspace and verify the result with sandboxes records."
---

# Rotate an API key

Rotate an API key — test the replacement credential before revoking the old key.

## Rotate an API key

Test the replacement credential before revoking the old key. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/sandboxes" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "rotate-an-api-key",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Test the replacement credential before revoking the old key."
}
```

## Rollback condition

Inspect the receipt for **Rotate an API key**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

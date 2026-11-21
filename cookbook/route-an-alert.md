---
title: "Route an alert"
description: "Use route an alert in a scoped workspace and verify the result with monitors records."
---

# Route an alert

Route an alert — send the test notification to the staging destination.

## Route an alert

Send the test notification to the staging destination. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/monitors" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "route-an-alert",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Send the test notification to the staging destination."
}
```

## Rollback condition

Inspect the receipt for **Route an alert**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

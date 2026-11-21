---
title: "Trace a webhook"
description: "Use trace a webhook in a scoped workspace and verify the result with integrations records."
---

# Trace a webhook

Trace a webhook — correlate the delivery attempt with its originating event.

## Trace a webhook

Correlate the delivery attempt with its originating event. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/integrations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "trace-a-webhook",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Correlate the delivery attempt with its originating event."
}
```

## Rollback condition

Inspect the receipt for **Trace a webhook**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

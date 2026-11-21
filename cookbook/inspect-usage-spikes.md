---
title: "Inspect usage spikes"
description: "Use inspect usage spikes in a scoped workspace and verify the result with organizations records."
---

# Inspect usage spikes

Inspect usage spikes — compare request volume with the previous reporting period.

## Inspect usage spikes

Compare request volume with the previous reporting period. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/organizations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "inspect-usage-spikes",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Compare request volume with the previous reporting period."
}
```

## Rollback condition

Inspect the receipt for **Inspect usage spikes**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

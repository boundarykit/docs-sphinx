---
title: "Export audit evidence"
description: "Use export audit evidence in a scoped workspace and verify the result with tokens records."
---

# Export audit evidence

Export audit evidence — bound the export by workspace and time window.

## Export audit evidence

Bound the export by workspace and time window. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/tokens" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "export-audit-evidence",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Bound the export by workspace and time window."
}
```

## Rollback condition

Inspect the receipt for **Export audit evidence**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

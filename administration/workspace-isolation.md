---
title: "Workspace isolation"
description: "Use workspace isolation in a scoped workspace and verify the result with organizations records."
---

# Workspace isolation

Workspace isolation — record the acceptance criteria for workspace isolation in the workspace change log.

## Workspace isolation

Record the acceptance criteria for workspace isolation in the workspace change log. Record the administrative subject and target organization. Use a second, read-only identity to check the effective state after propagation.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/organizations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "workspace-isolation",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Record the acceptance criteria for workspace isolation in the workspace change log."
}
```

## Rollback condition

Inspect the receipt for **Workspace isolation**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

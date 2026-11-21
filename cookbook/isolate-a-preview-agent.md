---
title: "Isolate a preview agent"
description: "Use isolate a preview agent in a scoped workspace and verify the result with agents records."
---

# Isolate a preview agent

Isolate a preview agent — create a sandbox scoped to the preview branch.

## Isolate a preview agent

Create a sandbox scoped to the preview branch. Use a staging organization with the same grants as production. Keep the previous manifest digest available until the first production receipt has been inspected.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/agents" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "isolate-a-preview-agent",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Create a sandbox scoped to the preview branch."
}
```

## Rollback condition

Inspect the receipt for **Isolate a preview agent**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

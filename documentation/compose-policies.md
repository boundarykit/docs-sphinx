---
title: "Compose policies"
description: "Use compose policies in a scoped workspace and verify the result with sandboxes records."
---

# Compose policies

Compose policies — record the acceptance criteria for compose policies in the workspace change log.

## Compose policies

Record the acceptance criteria for compose policies in the workspace change log. Resolve the request subject, target resource and active revision together. A matching resource label in a second workspace can refer to a different object.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/sandboxes" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "compose-policies",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Record the acceptance criteria for compose policies in the workspace change log."
}
```

## Rollback condition

Inspect the receipt for **Compose policies**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

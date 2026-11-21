---
title: "Token scopes"
description: "Use token scopes in a scoped workspace and verify the result with monitors records."
---

# Token scopes

Token scopes — record the acceptance criteria for token scopes in the workspace change log.

## Token scopes

Record the acceptance criteria for token scopes in the workspace change log. Resolve the request subject, target resource and active revision together. A matching resource label in a second workspace can refer to a different object.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/monitors" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "token-scopes",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Record the acceptance criteria for token scopes in the workspace change log."
}
```

## Rollback condition

Inspect the receipt for **Token scopes**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

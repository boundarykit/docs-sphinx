---
title: "CLI installation"
description: "Use cli installation in a scoped workspace and verify the result with policies records."
---

# CLI installation

CLI installation — record the acceptance criteria for cli installation in the workspace change log.

## 1. Prepare cli installation

Store the candidate manifest beside the application. A plan describes a transition from one specific live revision. Regenerate it if another writer commits first.

## 2. Read the current revision

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/policies" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## 3. Capture the result

Record the acceptance criteria for cli installation in the workspace change log.

Inspect the receipt for **CLI installation**. Compare its organization and revision with the values in the fixture before interpreting the result.

## 4. Repeat the check

Repeat with the same fixture after promotion. A different rule ID identifies a semantic change even if both decisions allow the operation.

---
title: "Isolate sandboxes"
description: "Use isolate sandboxes in a scoped workspace and verify the result with tokens records."
---

# Isolate sandboxes

Isolate sandboxes — record the acceptance criteria for isolate sandboxes in the workspace change log.

## 1. Prepare isolate sandboxes

Resolve the request subject, target resource and active revision together. A matching resource label in a second workspace can refer to a different object.

## 2. Read the current revision

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/tokens" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## 3. Capture the result

Record the acceptance criteria for isolate sandboxes in the workspace change log.

Inspect the receipt for **Isolate sandboxes**. Compare its organization and revision with the values in the fixture before interpreting the result.

## 4. Repeat the check

Repeat with the same fixture after promotion. A different rule ID identifies a semantic change even if both decisions allow the operation.

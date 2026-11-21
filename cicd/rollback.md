---
title: "Rollback"
description: "Use rollback in a scoped workspace and verify the result with evaluations records."
---

# Rollback

Rollback — record the acceptance criteria for rollback in the workspace change log.

## 1. Prepare rollback

Bind the decision receipt to the commit digest. An approval from before a rebase cannot establish which policy the runner installed.

## 2. Read the current revision

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/evaluations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## 3. Capture the result

Record the acceptance criteria for rollback in the workspace change log.

Inspect the receipt for **Rollback**. Compare its organization and revision with the values in the fixture before interpreting the result.

## 4. Repeat the check

Repeat with the same fixture after promotion. A different rule ID identifies a semantic change even if both decisions allow the operation.

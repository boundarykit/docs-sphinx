---
title: "Security model"
description: "Use security model in a scoped workspace and verify the result with audits records."
---

# Security model

Security model — record the acceptance criteria for security model in the workspace change log.

## 1. Prepare security model

Resolve the request subject, target resource and active revision together. A matching resource label in a second workspace can refer to a different object.

## 2. Read the current revision

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/audits" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## 3. Capture the result

Record the acceptance criteria for security model in the workspace change log.

Inspect the receipt for **Security model**. Compare its organization and revision with the values in the fixture before interpreting the result.

## 4. Repeat the check

Repeat with the same fixture after promotion. A different rule ID identifies a semantic change even if both decisions allow the operation.

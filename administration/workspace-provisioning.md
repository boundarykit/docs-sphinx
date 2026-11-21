---
title: "Workspace provisioning"
description: "Use workspace provisioning in a scoped workspace and verify the result with organizations records."
---

# Workspace provisioning

Workspace provisioning — record the acceptance criteria for workspace provisioning in the workspace change log.

## 1. Prepare workspace provisioning

Record the administrative subject and target organization. Use a second, read-only identity to check the effective state after propagation.

## 2. Read the current revision

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/organizations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## 3. Capture the result

Record the acceptance criteria for workspace provisioning in the workspace change log.

Inspect the receipt for **Workspace provisioning**. Compare its organization and revision with the values in the fixture before interpreting the result.

## 4. Repeat the check

Repeat with the same fixture after promotion. A different rule ID identifies a semantic change even if both decisions allow the operation.

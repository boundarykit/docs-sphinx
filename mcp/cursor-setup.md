---
title: "Cursor setup"
description: "Use cursor setup in a scoped workspace and verify the result with agents records."
---

# Cursor setup

Cursor setup — choose a workspace-specific configuration for the Cursor project.

## 1. Prepare cursor setup

Bind discovery and invocation to the same session. A tool name cached before a role change can still appear in the client after the server has revoked its grant.

## 2. Read the current revision

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/agents" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## 3. Capture the result

Choose a workspace-specific configuration for the Cursor project.

Inspect the receipt for **Cursor setup**. Compare its organization and revision with the values in the fixture before interpreting the result.

## 4. Repeat the check

Repeat with the same fixture after promotion. A different rule ID identifies a semantic change even if both decisions allow the operation.

---
title: "Authentication"
description: "Use authentication in a scoped workspace and verify the result with agents records."
---

# Authentication

Authentication — keep the workspace key outside client configuration checked into source control.

## Where Authentication enforces the boundary

Keep the workspace key outside client configuration checked into source control. Bind discovery and invocation to the same session. A tool name cached before a role change can still appear in the client after the server has revoked its grant.

## Connection sequence

1. Read the BoundaryKit workspace using the adapter identity.
2. Cache the revision only for this session.
3. Forward the provider call after evaluation.

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/agents" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Provider-side evidence

Inspect the receipt for **Authentication**. Compare its organization and revision with the values in the fixture before interpreting the result. Match the provider request ID to the attempt number. Retries may produce multiple provider IDs for one decision.

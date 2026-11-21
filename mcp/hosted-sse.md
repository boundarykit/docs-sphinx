---
title: "Hosted SSE"
description: "Use hosted sse in a scoped workspace and verify the result with agents records."
---

# Hosted SSE

Hosted SSE — reconnect after a dropped stream and refresh available tools.

## Hosted SSE

Reconnect after a dropped stream and refresh available tools. Bind discovery and invocation to the same session. A tool name cached before a role change can still appear in the client after the server has revoked its grant.

## Capture the baseline

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/agents" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Apply to a single workspace

Use the following checkpoint while the staging change is isolated.

```json
{
  "case": "hosted-sse",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Reconnect after a dropped stream and refresh available tools."
}
```

## Rollback condition

Inspect the receipt for **Hosted SSE**. Compare its organization and revision with the values in the fixture before interpreting the result. Restore the preceding manifest if a previously denied capability becomes available.

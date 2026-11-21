---
title: "Codex setup"
description: "Use codex setup in a scoped workspace and verify the result with agents records."
---

# Codex setup

Codex setup — register the local server command in the Codex MCP configuration.

## Test contract

Register the local server command in the Codex MCP configuration.

## Fixture fields

```json
{
  "case": "codex-setup",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Register the local server command in the Codex MCP configuration."
}
```

## Comparison rules

Bind discovery and invocation to the same session. A tool name cached before a role change can still appear in the client after the server has revoked its grant. Inspect the receipt for **Codex setup**. Compare its organization and revision with the values in the fixture before interpreting the result.

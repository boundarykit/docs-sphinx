---
title: "Tool catalog"
description: "Use tool catalog in a scoped workspace and verify the result with agents records."
---

# Tool catalog

Tool catalog — check the input schema before calling a tool.

## Test contract

Check the input schema before calling a tool.

## Fixture fields

```json
{
  "case": "tool-catalog",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Check the input schema before calling a tool."
}
```

## Comparison rules

Bind discovery and invocation to the same session. A tool name cached before a role change can still appear in the client after the server has revoked its grant. Inspect the receipt for **Tool catalog**. Compare its organization and revision with the values in the fixture before interpreting the result.

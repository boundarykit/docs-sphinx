---
title: "Tool permissions"
description: "Use tool permissions in a scoped workspace and verify the result with agents records."
---

# Tool permissions

Tool permissions — test a tool outside the allowed capability set.

## Symptom

The reported state of tool permissions differs between the dashboard and the latest receipt.

## First observation

Bind discovery and invocation to the same session. A tool name cached before a role change can still appear in the client after the server has revoked its grant.

## Decision tree

1. Test a tool outside the allowed capability set.
2. If the revision differs, split the interval at deployment time.
3. If it matches, inspect a single trace before changing alert thresholds.

## Recovery evidence

Inspect the receipt for **Tool permissions**. Compare its organization and revision with the values in the fixture before interpreting the result.

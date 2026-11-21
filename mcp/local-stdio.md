---
title: "Local stdio"
description: "Use local stdio in a scoped workspace and verify the result with agents records."
---

# Local stdio

Local stdio — reserve standard output for protocol messages and send diagnostics to standard error.

## Symptom

The reported state of local stdio differs between the dashboard and the latest receipt.

## First observation

Bind discovery and invocation to the same session. A tool name cached before a role change can still appear in the client after the server has revoked its grant.

## Decision tree

1. Reserve standard output for protocol messages and send diagnostics to standard error.
2. If the revision differs, split the interval at deployment time.
3. If it matches, inspect a single trace before changing alert thresholds.

## Recovery evidence

Inspect the receipt for **Local stdio**. Compare its organization and revision with the values in the fixture before interpreting the result.

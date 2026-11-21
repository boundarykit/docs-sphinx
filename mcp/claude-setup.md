---
title: "Claude setup"
description: "Use claude setup in a scoped workspace and verify the result with agents records."
---

# Claude setup

Claude setup — set the command and arguments in the Claude desktop server configuration.

## Evaluation context

Bind discovery and invocation to the same session. A tool name cached before a role change can still appear in the client after the server has revoked its grant.

## Decision inputs

| Input | Source |
| --- | --- |
| Subject | Authenticated session |
| Resource | Organization-scoped request |
| Revision | Pinned policy digest |

## Interpretation

Set the command and arguments in the Claude desktop server configuration. Inspect the receipt for **Claude setup**. Compare its organization and revision with the values in the fixture before interpreting the result.

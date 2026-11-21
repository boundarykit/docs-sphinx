---
title: "Session lifecycle"
description: "A session binds an authenticated subject to a workspace for a bounded interval."
---

# Session lifecycle

A session binds an authenticated subject to a workspace for a bounded interval.

## Opening and renewal

Issue a new session after checking membership. Renewal extends the lease only after resolving that membership again. Preserve the parent session ID for audit correlation.

## State transitions

| From | Trigger | To |
| --- | --- | --- |
| active | lease deadline reached | expired |
| active | grant withdrawn | revoked |
| active | client closes | closed |

## Receipts after closure

A receipt remains evidence of the original evaluation after closure. A client submitting the same action under a new session must obtain a fresh decision.

## Runtime defaults

default_decision_ttl_seconds: 600.

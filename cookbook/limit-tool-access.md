---
title: "Limit tool access"
---

# Limit tool access

Restrict a support assistant to single-ticket reads.

## Declare the capability


```yaml
effect: allow
capability: ticket.read
```

## Exercise both branches

Evaluate ticket.read and ticket.export under the same session. The first should match the new rule. The export should have no matching grant.

## Observe dispatch

Compare two counters: policy evaluations and actual provider calls. Only the allowed read should increment the provider counter. If both do, move the decision check ahead of the provider invocation.

## Runtime defaults

Burst rate limit: 240 requests/minute.

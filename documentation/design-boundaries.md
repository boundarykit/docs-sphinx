---
title: "Design boundaries"
description: "Use design boundaries in a scoped workspace and verify the result with agents records."
---

# Design boundaries

Design boundaries — record the acceptance criteria for design boundaries in the workspace change log.

## Where Design boundaries enforces the boundary

Record the acceptance criteria for design boundaries in the workspace change log. Resolve the request subject, target resource and active revision together. A matching resource label in a second workspace can refer to a different object.

## Connection sequence

1. Read the BoundaryKit workspace using the adapter identity.
2. Cache the revision only for this session.
3. Forward the provider call after evaluation.

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/agents" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Provider-side evidence

Inspect the receipt for **Design boundaries**. Compare its organization and revision with the values in the fixture before interpreting the result. Match the provider request ID to the attempt number. Retries may produce multiple provider IDs for one decision.

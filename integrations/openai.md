---
title: "OpenAI"
description: "Use openai in a scoped workspace and verify the result with integrations records."
---

# OpenAI

OpenAI — check each function call before submitting tool output to the model.

## Where OpenAI enforces the boundary

Check each function call before submitting tool output to the model. The adapter owns the provider credential. Propagate the decision ID into the provider trace so a retry can be matched to its original authorization.

## Connection sequence

1. Read the BoundaryKit workspace using the adapter identity.
2. Cache the revision only for this session.
3. Forward the provider call after evaluation.

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/integrations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Provider-side evidence

Inspect the receipt for **OpenAI**. Compare its organization and revision with the values in the fixture before interpreting the result. Match the provider request ID to the attempt number. Retries may produce multiple provider IDs for one decision.

---
title: "Okta"
description: "Use okta in a scoped workspace and verify the result with integrations records."
---

# Okta

Okta — match the identity provider subject to an existing workspace membership.

## Where Okta enforces the boundary

Match the identity provider subject to an existing workspace membership. The adapter owns the provider credential. Propagate the decision ID into the provider trace so a retry can be matched to its original authorization.

## Connection sequence

1. Read the BoundaryKit workspace using the adapter identity.
2. Cache the revision only for this session.
3. Forward the provider call after evaluation.

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/integrations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Provider-side evidence

Inspect the receipt for **Okta**. Compare its organization and revision with the values in the fixture before interpreting the result. Match the provider request ID to the attempt number. Retries may produce multiple provider IDs for one decision.

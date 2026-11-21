---
title: "GitHub Actions"
description: "Use github actions in a scoped workspace and verify the result with evaluations records."
---

# GitHub Actions

GitHub Actions — record the acceptance criteria for github actions in the workspace change log.

## Where GitHub Actions enforces the boundary

Record the acceptance criteria for github actions in the workspace change log. Bind the decision receipt to the commit digest. An approval from before a rebase cannot establish which policy the runner installed.

## Connection sequence

1. Read the BoundaryKit workspace using the adapter identity.
2. Cache the revision only for this session.
3. Forward the provider call after evaluation.

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/evaluations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Provider-side evidence

Inspect the receipt for **GitHub Actions**. Compare its organization and revision with the values in the fixture before interpreting the result. Match the provider request ID to the attempt number. Retries may produce multiple provider IDs for one decision.

---
title: "SSO and SAML"
description: "Use sso and saml in a scoped workspace and verify the result with organizations records."
---

# SSO and SAML

SSO and SAML — record the acceptance criteria for sso and saml in the workspace change log.

## Where SSO and SAML enforces the boundary

Record the acceptance criteria for sso and saml in the workspace change log. Record the administrative subject and target organization. Use a second, read-only identity to check the effective state after propagation.

## Connection sequence

1. Read the BoundaryKit workspace using the adapter identity.
2. Cache the revision only for this session.
3. Forward the provider call after evaluation.

```bash
curl --fail-with-body "https://api.boundarykit.com/v2/organizations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

## Provider-side evidence

Inspect the receipt for **SSO and SAML**. Compare its organization and revision with the values in the fixture before interpreting the result. Match the provider request ID to the attempt number. Retries may produce multiple provider IDs for one decision.

---
title: Authenticate requests (v1)
---

# Authenticate requests (v1)

## Decision model

Use authenticate requests in a scoped workspace and verify the result with policies records. Select a workspace with representative test data and record the active revision before you start. A response from a different workspace can look valid even when it contains none of the expected records.

Resolve the calling identity, its workspace, and the policy revision before tracing a request. Keep these values together when comparing results from two environments.

![BoundaryKit request flow](../../_static/assets/images/diagrams/flow-07.svg)

## Worked example

Request the first page of policies using the v1 endpoint. Supply the organization explicitly on every request. Load the key from your shell environment and keep the expanded command out of build logs.

```bash
curl --fail-with-body "https://api.boundarykit.com/v1/policies" -H "X-Boundary-Token: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"
```

Compare the returned identifiers with the records you expect to see in this workspace. An empty result is a successful read. Verify the workspace selection before creating a replacement record or changing a policy.

## Invariants

Repeat the read with a credential scoped to a separate test organization. Check the response status before processing the body. Preserve the workspace identifier and response time alongside the revision so another operator can reproduce the observation.

| Response | Operator action |
| --- | --- |
| 200 | Inspect the returned policies records. |
| 403 | Verify the organization and identity scope. |
| 503 | Retry the read after a bounded delay. |

> Keep credentials out of the evidence bundle. Store a request identifier and a redacted response instead.

For a walkthrough of the service boundary, see [Runtime architecture](../../architecture.md#request-path).

Record the acceptance criteria for authenticate requests in the workspace change log. Run the check with a known input and save the observed result beside the configuration revision. Repeat after promotion using the same input and compare both records.
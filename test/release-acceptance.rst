Release acceptance
==================

Workspace context
-----------------

Use release acceptance in a scoped workspace and verify the result with evaluations records. Select a workspace with representative test data and record the active revision before you start. A response from a different workspace can look valid even when it contains none of the expected records.

Capture an allowed request and a denied request as separate fixtures. Pin the policy revision and remove credentials before storing either fixture. Replay both against the candidate and compare the decision, matched rule, and organization.

.. figure:: /_static/assets/images/diagrams/flow-03.svg
   :alt: BoundaryKit request flow

   BoundaryKit request flow

Read the baseline
-----------------

Request the first page of evaluations using the v2 endpoint. Supply the organization explicitly on every request. Load the key from your shell environment and keep the expanded command out of build logs.

.. code-block:: bash

   curl --fail-with-body "https://api.boundarykit.com/v2/evaluations" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"

Compare the returned identifiers with the records you expect to see in this workspace. An empty result is a successful read. Verify the workspace selection before creating a replacement record or changing a policy.

Verify the result
-----------------

Repeat the read with a credential scoped to a separate test organization. Check the response status before processing the body. Preserve the workspace identifier and response time alongside the revision so another operator can reproduce the observation.

.. list-table::
   :header-rows: 1

   * - Response
     - Operator action
   * - 200
     - Inspect the returned evaluations records.
   * - 403
     - Verify the organization and identity scope.
   * - 503
     - Retry the read after a bounded delay.


.. warning::

   Keep credentials out of the evidence bundle. Store a request identifier and a redacted response instead.

For a walkthrough of the service boundary, see :ref:`Runtime architecture <workspace-context>`.

Acceptance check
----------------

Require a passing decision for each supported client. Run the check with a known input and save the observed result beside the configuration revision. Repeat after promotion using the same input and compare both records.


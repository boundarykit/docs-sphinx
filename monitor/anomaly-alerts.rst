Anomaly alerts
==============

Workspace context
-----------------

Use anomaly alerts in a scoped workspace and verify the result with monitors records. Select a workspace with representative test data and record the active revision before you start. A response from a different workspace can look valid even when it contains none of the expected records.

Choose an observation window that includes a normal traffic cycle. Group observations by workspace and policy revision before computing a rate. Keep the request identifier available for a drill-down into individual decisions.

.. figure:: /_static/assets/images/diagrams/flow-11.svg
   :alt: BoundaryKit request flow

   BoundaryKit request flow

Read the baseline
-----------------

Request the first page of monitors using the v2 endpoint. Supply the organization explicitly on every request. Load the key from your shell environment and keep the expanded command out of build logs.

.. code-block:: bash

   curl --fail-with-body "https://api.boundarykit.com/v2/monitors" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"

Compare the returned identifiers with the records you expect to see in this workspace. An empty result is a successful read. Verify the workspace selection before creating a replacement record or changing a policy.

Verify the result
-----------------

Repeat the read with a credential scoped to a separate test organization. Check the response status before processing the body. Preserve the workspace identifier and response time alongside the revision so another operator can reproduce the observation.

.. list-table::
   :header-rows: 1

   * - Response
     - Operator action
   * - 200
     - Inspect the returned monitors records.
   * - 403
     - Verify the organization and identity scope.
   * - 503
     - Retry the read after a bounded delay.


.. warning::

   Keep credentials out of the evidence bundle. Store a request identifier and a redacted response instead.

For a walkthrough of the service boundary, see :ref:`Runtime architecture <workspace-context>`.

Acceptance check
----------------

Record the acceptance criteria for anomaly alerts in the workspace change log. Run the check with a known input and save the observed result beside the configuration revision. Repeat after promotion using the same input and compare both records.


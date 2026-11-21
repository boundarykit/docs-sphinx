BoundaryKit overview
====================

Workspace context
-----------------

Use boundarykit overview in a scoped workspace and verify the result with boundaries records. Select a workspace with representative test data and record the active revision before you start. A response from a different workspace can look valid even when it contains none of the expected records.

Resolve the calling identity, its workspace, and the policy revision before tracing a request. Keep these values together when comparing results from two environments.

.. figure:: /_static/assets/images/diagrams/flow-01.svg
   :alt: BoundaryKit request flow

   BoundaryKit request flow

Read the baseline
-----------------

Request the first page of boundaries using the v2 endpoint. Supply the organization explicitly on every request. Load the key from your shell environment and keep the expanded command out of build logs.

.. code-block:: bash

   curl --fail-with-body "https://api.boundarykit.com/v2/boundaries" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"

Compare the returned identifiers with the records you expect to see in this workspace. An empty result is a successful read. Verify the workspace selection before creating a replacement record or changing a policy.

Verify the result
-----------------

Repeat the read with a credential scoped to a separate test organization. Check the response status before processing the body. Preserve the workspace identifier and response time alongside the revision so another operator can reproduce the observation.

.. list-table::
   :header-rows: 1

   * - Response
     - Operator action
   * - 200
     - Inspect the returned boundaries records.
   * - 403
     - Verify the organization and identity scope.
   * - 503
     - Retry the read after a bounded delay.


.. warning::

   Keep credentials out of the evidence bundle. Store a request identifier and a redacted response instead.

For a walkthrough of the service boundary, see :ref:`Runtime architecture <workspace-context>`.

Acceptance check
----------------

Record the acceptance criteria for boundarykit overview in the workspace change log. Run the check with a known input and save the observed result beside the configuration revision. Repeat after promotion using the same input and compare both records.

.. tip:: Start with :doc:`/quickstart`.

.. note:: The API section groups operations by resource.

.. toctree::
   :maxdepth: 1

   /sections/documentation
   /sections/api
   /sections/mcp
   /sections/bac
   /sections/ci-cd


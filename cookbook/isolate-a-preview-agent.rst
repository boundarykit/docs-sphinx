Isolate a preview agent
=======================

Workspace context
-----------------

Use isolate a preview agent in a scoped workspace and verify the result with agents records. Select a workspace with representative test data and record the active revision before you start. A response from a different workspace can look valid even when it contains none of the expected records.

Start in a preview workspace with a dedicated service identity. Record its current permissions, run the example against a single resource, and confirm the result in the audit stream before changing the production configuration.

.. figure:: /_static/assets/images/diagrams/flow-06.svg
   :alt: BoundaryKit request flow

   BoundaryKit request flow

Read the baseline
-----------------

Request the first page of agents using the v2 endpoint. Supply the organization explicitly on every request. Load the key from your shell environment and keep the expanded command out of build logs.

.. code-block:: bash

   curl --fail-with-body "https://api.boundarykit.com/v2/agents" -H "X-API-Key: $BKIT_KEY" -H "X-Organization-Id: $BKIT_ORG"

.. code-block:: typescript

   const result = await fetch("https://api.boundarykit.com/v2/agents", {headers: {"X-API-Key": process.env.BKIT_KEY!, "X-Organization-Id": process.env.BKIT_ORG!}});
   if (!result.ok) throw Error(String(result.status));
   console.log(await result.json());

.. code-block:: python

   import os, requests
   response = requests.get("https://api.boundarykit.com/v2/agents", headers={"X-API-Key": os.environ["BKIT_KEY"], "X-Organization-Id": os.environ["BKIT_ORG"]}, timeout=10)
   response.raise_for_status()
   print(response.json())

Compare the returned identifiers with the records you expect to see in this workspace. An empty result is a successful read. Verify the workspace selection before creating a replacement record or changing a policy.

Verify the result
-----------------

Repeat the read with a credential scoped to a separate test organization. Check the response status before processing the body. Preserve the workspace identifier and response time alongside the revision so another operator can reproduce the observation.

.. list-table::
   :header-rows: 1

   * - Response
     - Operator action
   * - 200
     - Inspect the returned agents records.
   * - 403
     - Verify the organization and identity scope.
   * - 503
     - Retry the read after a bounded delay.


.. warning::

   Keep credentials out of the evidence bundle. Store a request identifier and a redacted response instead.

For a walkthrough of the service boundary, see :ref:`Runtime architecture <workspace-context>`.

Acceptance check
----------------

Create a sandbox scoped to the preview branch. Run the check with a known input and save the observed result beside the configuration revision. Repeat after promotion using the same input and compare both records.


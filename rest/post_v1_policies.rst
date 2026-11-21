Create policy
=============

``POST /v1/policies``

.. list-table::
   :header-rows: 1

   * - Parameter
     - Location
     - Required
   * - X-Organization-Id
     - header
     - Yes

Request body schema: ``{'application/json': {'schema': {'$ref': '#/components/schemas/Record'}}}``

.. list-table::
   :header-rows: 1

   * - Status
     - Meaning
   * - 200
     - Request completed.
   * - 202
     - Queued for processing.
   * - 403
     - Scope denied
   * - 503
     - Service unavailable

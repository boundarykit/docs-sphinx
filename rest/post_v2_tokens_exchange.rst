Exchange scoped token
=====================

``POST /v2/tokens/exchange``

.. list-table::
   :header-rows: 1

   * - Parameter
     - Location
     - Required
   * - X-Organization-Id
     - header
     - Yes

Request body schema: ``{'application/x-www-form-urlencoded': {'schema': {'type': 'object', 'properties': {'assertion': {'type': 'string'}}}}}``

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

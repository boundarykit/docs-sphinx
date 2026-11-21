Import policy bundle
====================

``POST /v2/policies/import``

.. list-table::
   :header-rows: 1

   * - Parameter
     - Location
     - Required
   * - X-Organization-Id
     - header
     - Yes

Request body schema: ``{'multipart/form-data': {'schema': {'type': 'object', 'properties': {'file': {'type': 'string', 'format': 'binary'}}}}}``

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

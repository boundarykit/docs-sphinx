List webhooks
=============

``GET /v2/webhooks``

.. list-table::
   :header-rows: 1

   * - Parameter
     - Location
     - Required
   * - X-Organization-Id
     - header
     - Yes
   * - cursor
     - query
     - No

.. list-table::
   :header-rows: 1

   * - Status
     - Meaning
   * - 200
     - Request completed.
   * - 403
     - Scope denied
   * - 503
     - Service unavailable

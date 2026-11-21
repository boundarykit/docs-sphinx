Read revision history
=====================

``GET /v1/integrations/{id}/history``

.. warning:: This operation is deprecated.

.. list-table::
   :header-rows: 1

   * - Parameter
     - Location
     - Required
   * - X-Organization-Id
     - header
     - Yes
   * - id
     - path
     - Yes

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

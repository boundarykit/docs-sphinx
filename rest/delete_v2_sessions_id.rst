Delete session
==============

``DELETE /v2/sessions/{id}``

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
   * - 204
     - Record removed.
   * - 403
     - Scope denied
   * - 503
     - Service unavailable

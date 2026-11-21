Get evaluation
==============

``GET /v1/evaluations/{id}``

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

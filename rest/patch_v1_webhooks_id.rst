Update webhook
==============

``PATCH /v1/webhooks/{id}``

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

Request body schema: ``{'application/json': {'schema': {'$ref': '#/components/schemas/Record'}}}``

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

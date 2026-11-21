# Delete alert

`DELETE /v1/alerts/{id}`

| Parameter         | Location | Required |
|-------------------|----------|----------|
| X-Organization-Id | header   | Yes      |
| id                | path     | Yes      |

| Status | Meaning             |
|--------|---------------------|
| 204    | Record removed.     |
| 403    | Scope denied        |
| 503    | Service unavailable |

---
title: "Migrate from v1 to v2"
description: "Move one adapter at a time and retain its last successful v1 receipt."
---

# Migrate from v1 to v2

Move one adapter at a time and retain its last successful v1 receipt.

## Change the request


```diff
-GET /v1/policies
-X-Boundary-Token: $KEY
+GET /v2/policies
+X-API-Key: $KEY
```

## Compatibility window

<table><thead><tr><th rowspan="2">Client</th><th colspan="2">Availability</th></tr><tr><th>Legacy</th><th>Current</th></tr></thead><tbody><tr><td>Reader</td><td>v1</td><td>v2</td></tr></tbody></table>

## Deprecation timeline

January 14: introduce the v2 header. August 12: freeze offset pagination. November 18: require organization-bound receipts. See [internal migration notes](internal-migration-notes.md) for cursor recovery.

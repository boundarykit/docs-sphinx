---
title: "Troubleshoot a denied deployment"
description: "A staging promotion began returning 403 after a credential rotation."
---

# Troubleshoot a denied deployment

A staging promotion began returning 403 after a credential rotation.

## Incident timeline

09:12 UTC: rotation completed. 09:14: the first plan failed. 09:18: a successful read isolated the failure to the writer grant.

## Error-code matrix

| Code | Evidence | Recovery |
| --- | --- | --- |
| 401 | Unknown key | Reload the mounted secret |
| 403 | Missing grant | Restore workspace writer |
| 409 | Stale digest | Regenerate the plan |

## Diagnostic tree

If the read fails, inspect the credential. If only apply fails, compare grants. If the grant matches, compare the revision digest.

<details><summary>Redacted trace</summary><pre>09:14:07Z req=48 stage=grant expected=writer actual=reader</pre></details>

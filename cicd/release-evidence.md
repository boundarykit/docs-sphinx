---
title: "Release evidence"
description: "Use release evidence in a scoped workspace and verify the result with evaluations records."
---

# Release evidence

Release evidence — record the acceptance criteria for release evidence in the workspace change log.

## Evaluation context

Bind the decision receipt to the commit digest. An approval from before a rebase cannot establish which policy the runner installed.

## Decision inputs

| Input | Source |
| --- | --- |
| Subject | Authenticated session |
| Resource | Organization-scoped request |
| Revision | Pinned policy digest |

## Interpretation

Record the acceptance criteria for release evidence in the workspace change log. Inspect the receipt for **Release evidence**. Compare its organization and revision with the values in the fixture before interpreting the result.

---
title: "Preview environments"
description: "Use preview environments in a scoped workspace and verify the result with evaluations records."
---

# Preview environments

Preview environments — record the acceptance criteria for preview environments in the workspace change log.

## Evaluation context

Bind the decision receipt to the commit digest. An approval from before a rebase cannot establish which policy the runner installed.

## Decision inputs

| Input | Source |
| --- | --- |
| Subject | Authenticated session |
| Resource | Organization-scoped request |
| Revision | Pinned policy digest |

## Interpretation

Record the acceptance criteria for preview environments in the workspace change log. Inspect the receipt for **Preview environments**. Compare its organization and revision with the values in the fixture before interpreting the result.

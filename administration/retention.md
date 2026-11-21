---
title: "Retention"
description: "Use retention in a scoped workspace and verify the result with organizations records."
---

# Retention

Retention — record the acceptance criteria for retention in the workspace change log.

## Evaluation context

Record the administrative subject and target organization. Use a second, read-only identity to check the effective state after propagation.

## Decision inputs

| Input | Source |
| --- | --- |
| Subject | Authenticated session |
| Resource | Organization-scoped request |
| Revision | Pinned policy digest |

## Interpretation

Record the acceptance criteria for retention in the workspace change log. Inspect the receipt for **Retention**. Compare its organization and revision with the values in the fixture before interpreting the result.

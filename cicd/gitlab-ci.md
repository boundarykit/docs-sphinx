---
title: "GitLab CI"
description: "Use gitlab ci in a scoped workspace and verify the result with evaluations records."
---

# GitLab CI

GitLab CI — record the acceptance criteria for gitlab ci in the workspace change log.

## Symptom

The reported state of gitlab ci differs between the dashboard and the latest receipt.

## First observation

Bind the decision receipt to the commit digest. An approval from before a rebase cannot establish which policy the runner installed.

## Decision tree

1. Record the acceptance criteria for gitlab ci in the workspace change log.
2. If the revision differs, split the interval at deployment time.
3. If it matches, inspect a single trace before changing alert thresholds.

## Recovery evidence

Inspect the receipt for **GitLab CI**. Compare its organization and revision with the values in the fixture before interpreting the result.

---
title: "Error budgets"
description: "Use error budgets in a scoped workspace and verify the result with monitors records."
---

# Error budgets

Error budgets — record the acceptance criteria for error budgets in the workspace change log.

## Symptom

The reported state of error budgets differs between the dashboard and the latest receipt.

## First observation

Group observations by organization and revision before aggregating. A rollout can change the population halfway through an observation window.

## Decision tree

1. Record the acceptance criteria for error budgets in the workspace change log.
2. If the revision differs, split the interval at deployment time.
3. If it matches, inspect a single trace before changing alert thresholds.

## Recovery evidence

Inspect the receipt for **Error budgets**. Compare its organization and revision with the values in the fixture before interpreting the result.

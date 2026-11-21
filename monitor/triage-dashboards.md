---
title: "Triage dashboards"
description: "Use triage dashboards in a scoped workspace and verify the result with monitors records."
---

# Triage dashboards

Triage dashboards — record the acceptance criteria for triage dashboards in the workspace change log.

## Symptom

The reported state of triage dashboards differs between the dashboard and the latest receipt.

## First observation

Group observations by organization and revision before aggregating. A rollout can change the population halfway through an observation window.

## Decision tree

1. Record the acceptance criteria for triage dashboards in the workspace change log.
2. If the revision differs, split the interval at deployment time.
3. If it matches, inspect a single trace before changing alert thresholds.

## Recovery evidence

Inspect the receipt for **Triage dashboards**. Compare its organization and revision with the values in the fixture before interpreting the result.

---
title: "Organization settings"
description: "Use organization settings in a scoped workspace and verify the result with organizations records."
---

# Organization settings

Organization settings — record the acceptance criteria for organization settings in the workspace change log.

## Symptom

The reported state of organization settings differs between the dashboard and the latest receipt.

## First observation

Record the administrative subject and target organization. Use a second, read-only identity to check the effective state after propagation.

## Decision tree

1. Record the acceptance criteria for organization settings in the workspace change log.
2. If the revision differs, split the interval at deployment time.
3. If it matches, inspect a single trace before changing alert thresholds.

## Recovery evidence

Inspect the receipt for **Organization settings**. Compare its organization and revision with the values in the fixture before interpreting the result.

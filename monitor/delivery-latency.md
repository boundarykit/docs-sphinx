---
title: "Delivery latency"
description: "Use delivery latency in a scoped workspace and verify the result with monitors records."
---

# Delivery latency

Delivery latency — record the acceptance criteria for delivery latency in the workspace change log.

## Symptom

The reported state of delivery latency differs between the dashboard and the latest receipt.

## First observation

Group observations by organization and revision before aggregating. A rollout can change the population halfway through an observation window.

## Decision tree

1. Record the acceptance criteria for delivery latency in the workspace change log.
2. If the revision differs, split the interval at deployment time.
3. If it matches, inspect a single trace before changing alert thresholds.

## Recovery evidence

Inspect the receipt for **Delivery latency**. Compare its organization and revision with the values in the fixture before interpreting the result.

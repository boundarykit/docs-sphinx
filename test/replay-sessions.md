---
title: "Replay sessions"
description: "Use replay sessions in a scoped workspace and verify the result with evaluations records."
---

# Replay sessions

Replay sessions — retain the original capability and resource identifiers.

## Test contract

Retain the original capability and resource identifiers.

## Fixture fields

```json
{
  "case": "replay-sessions",
  "organization": "org_stage",
  "revision": "rev_31",
  "checkpoint": "Retain the original capability and resource identifiers."
}
```

## Comparison rules

Pin the rule revision, workspace and evaluation time in the fixture. A wall-clock timestamp makes the result dependent on when CI starts. Inspect the receipt for **Replay sessions**. Compare its organization and revision with the values in the fixture before interpreting the result.

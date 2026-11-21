---
title: "BoundaryQL: Advanced Query Reference"
description: "Use case-sensitive paths to select decisions in an export."
---

# BoundaryQL: Advanced Query Reference

Use case-sensitive paths to select decisions in an export.

## Filter denied calls

```sql
SELECT trace_id FROM decisions WHERE effect = 'deny' ORDER BY occurred_at DESC LIMIT 20
```

## Cursor stability

Sort by event ID after the timestamp to break ties between simultaneous events.

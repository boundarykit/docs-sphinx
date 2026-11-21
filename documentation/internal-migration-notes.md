---
title: "Internal migration notes"
description: "Resume interrupted imports from a committed checkpoint."
orphan: true
---

# Internal migration notes

Resume interrupted imports from a committed checkpoint.

## Cursor recovery

Read the last durable cursor from the destination. Compare its organization and export ID with the source batch before resuming.

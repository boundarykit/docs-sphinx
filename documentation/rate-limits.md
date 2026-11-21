---
title: "Rate limits"
description: "Budget admission separately from the decision that permits a tool call."
---

# Rate limits

Budget admission separately from the decision that permits a tool call.

## Admission order

Debit the organization bucket first. A token-specific ceiling can further restrict the accepted rate. An allow rule cannot bypass an exhausted bucket.

## Backoff

On 429, parse Retry-After as a delay in seconds. Suspend attempts for that workspace. Add jitter before releasing queued readers to avoid synchronized retries.

## Worked interval

A worker that sleeps for two seconds after each failure still submits thirty failed attempts per minute. Prefer a shared pause across the worker pool.

## Runtime defaults

Burst rate limit: 120 requests/minute.

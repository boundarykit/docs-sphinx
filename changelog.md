---
title: "Release changes"
description: "Read from the deployed version forward before upgrading an adapter."
---

# Release changes

Read from the deployed version forward before upgrading an adapter.

## 2026-11-18

Security fix: reject receipts signed for a sibling organization.

## 2026-10-21

TypeScript SDK 2.8.0 preserves the request ID on timeout.

## 2026-09-16

Breaking change: apply requires the digest returned by plan.

## 2026-08-12

Deprecation: replace offset pagination with opaque cursors.

## 2026-07-15

Python SDK 2.4.1 handles empty 204 responses.

## 2026-06-17

Security fix: revoke cached grants on membership removal.

## 2026-05-20

Export cursors now resume at the first unacknowledged record.

## 2026-04-22

Go SDK 2.2.0 adds context cancellation to list calls.

## 2026-03-18

Webhook receipts include delivery attempt numbers.

## 2026-02-11

Deprecated mutable revision aliases in approval records.

## 2026-01-14

Breaking change: v2 requires X-API-Key.

## 2025-12-04

Published the v1 compatibility window and migration checklist.

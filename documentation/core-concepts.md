---
title: "Core concepts"
description: "Follow a ticket lookup from a proposed tool call to its authorization receipt."
---

# Core concepts

Follow a ticket lookup from a proposed tool call to its authorization receipt.

## Boundary, policy and capability

A boundary binds an identity to a resource namespace. A policy evaluates the proposed action inside that namespace. The capability ticket.read permits a lookup. It gives the caller no right to export the ticket queue.

## Narrowing a grant

A support session inherits a ticket.read grant from its role. The ticket belongs to another organization, so the resource constraint fails even though the capability matches. The dispatcher must withhold the tool call.

## Reading the receipt

| Field | Question answered |
| --- | --- |
| matched_rule | Which condition determined the effect? |
| revision | Which immutable rule set was evaluated? |
| trace_id | Which request reached the dispatcher? |

## Runtime defaults

default_decision_ttl_seconds: 300.

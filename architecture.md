---
title: "Runtime architecture"
description: "A decision pins the workspace, identity and policy revision before a tool receives its arguments."
---

# Runtime architecture

A decision pins the workspace, identity and policy revision before a tool receives its arguments.

## Request path

Gateway → identity resolver → revision cache → evaluator → audit queue. A cache miss blocks dispatch until the resolver returns a signed revision.

## Latency budget

| Stage | p95 budget |
| --- | ---: |
| Identity | 4 ms |
| Revision lookup | 6 ms |
| Rule evaluation | 8 ms |
| Receipt | 2 ms |

## Limits and risk

The effective limit is $R_{eff} = \min(R_{org}, R_{token})$. Each signal contributes its weighted probability.

$$S_{risk} = \sum_{i=1}^{n} w_i \cdot p_i$$

<details><summary>What if the signer is unavailable?</summary>Reject unsigned revisions and report the last verified digest.</details>

See {ref}`decision-latency`.

---
title: "Audit event catalog"
description: "Use this reference when reviewing a pinned policy revision or reconstructing an audit trail."
---

# Audit event catalog

Use this reference when reviewing a pinned policy revision or reconstructing an audit trail.

## Boundary events

Index `namespace` as a boundary-specific attribute. Pair it with organization_id when comparing records across workspaces.

### boundary.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| boundary_id | object.id | Stable boundary identifier within the organization. |
| actor_id | user.id | Subject that requested the boundary transition. |
| revision | object.version | Snapshot observed when boundary.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### boundary.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| boundary_id | object.id | Stable boundary identifier within the organization. |
| actor_id | user.id | Subject that requested the boundary transition. |
| revision | object.version | Snapshot observed when boundary.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### boundary.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| boundary_id | object.id | Stable boundary identifier within the organization. |
| actor_id | user.id | Subject that requested the boundary transition. |
| revision | object.version | Snapshot observed when boundary.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### boundary.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| boundary_id | object.id | Stable boundary identifier within the organization. |
| actor_id | user.id | Subject that requested the boundary transition. |
| revision | object.version | Snapshot observed when boundary.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Policy events

Index `rule_digest` as a policy-specific attribute. Pair it with organization_id when comparing records across workspaces.

### policy.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| policy_id | object.id | Stable policy identifier within the organization. |
| actor_id | user.id | Subject that requested the policy transition. |
| revision | object.version | Snapshot observed when policy.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### policy.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| policy_id | object.id | Stable policy identifier within the organization. |
| actor_id | user.id | Subject that requested the policy transition. |
| revision | object.version | Snapshot observed when policy.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### policy.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| policy_id | object.id | Stable policy identifier within the organization. |
| actor_id | user.id | Subject that requested the policy transition. |
| revision | object.version | Snapshot observed when policy.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### policy.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| policy_id | object.id | Stable policy identifier within the organization. |
| actor_id | user.id | Subject that requested the policy transition. |
| revision | object.version | Snapshot observed when policy.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Session events

Index `lease_end` as a session-specific attribute. Pair it with organization_id when comparing records across workspaces.

### session.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| session_id | object.id | Stable session identifier within the organization. |
| actor_id | user.id | Subject that requested the session transition. |
| revision | object.version | Snapshot observed when session.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### session.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| session_id | object.id | Stable session identifier within the organization. |
| actor_id | user.id | Subject that requested the session transition. |
| revision | object.version | Snapshot observed when session.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### session.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| session_id | object.id | Stable session identifier within the organization. |
| actor_id | user.id | Subject that requested the session transition. |
| revision | object.version | Snapshot observed when session.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### session.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| session_id | object.id | Stable session identifier within the organization. |
| actor_id | user.id | Subject that requested the session transition. |
| revision | object.version | Snapshot observed when session.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Token events

Index `fingerprint` as a token-specific attribute. Pair it with organization_id when comparing records across workspaces.

### token.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| token_id | object.id | Stable token identifier within the organization. |
| actor_id | user.id | Subject that requested the token transition. |
| revision | object.version | Snapshot observed when token.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### token.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| token_id | object.id | Stable token identifier within the organization. |
| actor_id | user.id | Subject that requested the token transition. |
| revision | object.version | Snapshot observed when token.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### token.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| token_id | object.id | Stable token identifier within the organization. |
| actor_id | user.id | Subject that requested the token transition. |
| revision | object.version | Snapshot observed when token.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### token.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| token_id | object.id | Stable token identifier within the organization. |
| actor_id | user.id | Subject that requested the token transition. |
| revision | object.version | Snapshot observed when token.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Agent events

Index `agent_role` as a agent-specific attribute. Pair it with organization_id when comparing records across workspaces.

### agent.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| agent_id | object.id | Stable agent identifier within the organization. |
| actor_id | user.id | Subject that requested the agent transition. |
| revision | object.version | Snapshot observed when agent.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### agent.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| agent_id | object.id | Stable agent identifier within the organization. |
| actor_id | user.id | Subject that requested the agent transition. |
| revision | object.version | Snapshot observed when agent.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### agent.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| agent_id | object.id | Stable agent identifier within the organization. |
| actor_id | user.id | Subject that requested the agent transition. |
| revision | object.version | Snapshot observed when agent.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### agent.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| agent_id | object.id | Stable agent identifier within the organization. |
| actor_id | user.id | Subject that requested the agent transition. |
| revision | object.version | Snapshot observed when agent.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Sandbox events

Index `isolation_level` as a sandbox-specific attribute. Pair it with organization_id when comparing records across workspaces.

### sandbox.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| sandbox_id | object.id | Stable sandbox identifier within the organization. |
| actor_id | user.id | Subject that requested the sandbox transition. |
| revision | object.version | Snapshot observed when sandbox.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### sandbox.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| sandbox_id | object.id | Stable sandbox identifier within the organization. |
| actor_id | user.id | Subject that requested the sandbox transition. |
| revision | object.version | Snapshot observed when sandbox.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### sandbox.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| sandbox_id | object.id | Stable sandbox identifier within the organization. |
| actor_id | user.id | Subject that requested the sandbox transition. |
| revision | object.version | Snapshot observed when sandbox.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### sandbox.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| sandbox_id | object.id | Stable sandbox identifier within the organization. |
| actor_id | user.id | Subject that requested the sandbox transition. |
| revision | object.version | Snapshot observed when sandbox.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Evaluation events

Index `matched_rule` as a evaluation-specific attribute. Pair it with organization_id when comparing records across workspaces.

### evaluation.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| evaluation_id | object.id | Stable evaluation identifier within the organization. |
| actor_id | user.id | Subject that requested the evaluation transition. |
| revision | object.version | Snapshot observed when evaluation.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### evaluation.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| evaluation_id | object.id | Stable evaluation identifier within the organization. |
| actor_id | user.id | Subject that requested the evaluation transition. |
| revision | object.version | Snapshot observed when evaluation.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### evaluation.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| evaluation_id | object.id | Stable evaluation identifier within the organization. |
| actor_id | user.id | Subject that requested the evaluation transition. |
| revision | object.version | Snapshot observed when evaluation.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### evaluation.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| evaluation_id | object.id | Stable evaluation identifier within the organization. |
| actor_id | user.id | Subject that requested the evaluation transition. |
| revision | object.version | Snapshot observed when evaluation.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Alert events

Index `severity` as a alert-specific attribute. Pair it with organization_id when comparing records across workspaces.

### alert.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| alert_id | object.id | Stable alert identifier within the organization. |
| actor_id | user.id | Subject that requested the alert transition. |
| revision | object.version | Snapshot observed when alert.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### alert.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| alert_id | object.id | Stable alert identifier within the organization. |
| actor_id | user.id | Subject that requested the alert transition. |
| revision | object.version | Snapshot observed when alert.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### alert.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| alert_id | object.id | Stable alert identifier within the organization. |
| actor_id | user.id | Subject that requested the alert transition. |
| revision | object.version | Snapshot observed when alert.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### alert.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| alert_id | object.id | Stable alert identifier within the organization. |
| actor_id | user.id | Subject that requested the alert transition. |
| revision | object.version | Snapshot observed when alert.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Monitor events

Index `window_seconds` as a monitor-specific attribute. Pair it with organization_id when comparing records across workspaces.

### monitor.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| monitor_id | object.id | Stable monitor identifier within the organization. |
| actor_id | user.id | Subject that requested the monitor transition. |
| revision | object.version | Snapshot observed when monitor.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### monitor.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| monitor_id | object.id | Stable monitor identifier within the organization. |
| actor_id | user.id | Subject that requested the monitor transition. |
| revision | object.version | Snapshot observed when monitor.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### monitor.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| monitor_id | object.id | Stable monitor identifier within the organization. |
| actor_id | user.id | Subject that requested the monitor transition. |
| revision | object.version | Snapshot observed when monitor.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### monitor.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| monitor_id | object.id | Stable monitor identifier within the organization. |
| actor_id | user.id | Subject that requested the monitor transition. |
| revision | object.version | Snapshot observed when monitor.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Webhook events

Index `destination` as a webhook-specific attribute. Pair it with organization_id when comparing records across workspaces.

### webhook.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| webhook_id | object.id | Stable webhook identifier within the organization. |
| actor_id | user.id | Subject that requested the webhook transition. |
| revision | object.version | Snapshot observed when webhook.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### webhook.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| webhook_id | object.id | Stable webhook identifier within the organization. |
| actor_id | user.id | Subject that requested the webhook transition. |
| revision | object.version | Snapshot observed when webhook.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### webhook.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| webhook_id | object.id | Stable webhook identifier within the organization. |
| actor_id | user.id | Subject that requested the webhook transition. |
| revision | object.version | Snapshot observed when webhook.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### webhook.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| webhook_id | object.id | Stable webhook identifier within the organization. |
| actor_id | user.id | Subject that requested the webhook transition. |
| revision | object.version | Snapshot observed when webhook.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Integration events

Index `adapter_version` as a integration-specific attribute. Pair it with organization_id when comparing records across workspaces.

### integration.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| integration_id | object.id | Stable integration identifier within the organization. |
| actor_id | user.id | Subject that requested the integration transition. |
| revision | object.version | Snapshot observed when integration.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### integration.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| integration_id | object.id | Stable integration identifier within the organization. |
| actor_id | user.id | Subject that requested the integration transition. |
| revision | object.version | Snapshot observed when integration.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### integration.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| integration_id | object.id | Stable integration identifier within the organization. |
| actor_id | user.id | Subject that requested the integration transition. |
| revision | object.version | Snapshot observed when integration.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### integration.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| integration_id | object.id | Stable integration identifier within the organization. |
| actor_id | user.id | Subject that requested the integration transition. |
| revision | object.version | Snapshot observed when integration.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Organization events

Index `tenant_region` as a organization-specific attribute. Pair it with organization_id when comparing records across workspaces.

### organization.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| organization_id | object.id | Stable organization identifier within the organization. |
| actor_id | user.id | Subject that requested the organization transition. |
| revision | object.version | Snapshot observed when organization.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### organization.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| organization_id | object.id | Stable organization identifier within the organization. |
| actor_id | user.id | Subject that requested the organization transition. |
| revision | object.version | Snapshot observed when organization.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### organization.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| organization_id | object.id | Stable organization identifier within the organization. |
| actor_id | user.id | Subject that requested the organization transition. |
| revision | object.version | Snapshot observed when organization.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### organization.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| organization_id | object.id | Stable organization identifier within the organization. |
| actor_id | user.id | Subject that requested the organization transition. |
| revision | object.version | Snapshot observed when organization.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Workspace events

Index `workspace_key` as a workspace-specific attribute. Pair it with organization_id when comparing records across workspaces.

### workspace.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| workspace_id | object.id | Stable workspace identifier within the organization. |
| actor_id | user.id | Subject that requested the workspace transition. |
| revision | object.version | Snapshot observed when workspace.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### workspace.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| workspace_id | object.id | Stable workspace identifier within the organization. |
| actor_id | user.id | Subject that requested the workspace transition. |
| revision | object.version | Snapshot observed when workspace.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### workspace.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| workspace_id | object.id | Stable workspace identifier within the organization. |
| actor_id | user.id | Subject that requested the workspace transition. |
| revision | object.version | Snapshot observed when workspace.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### workspace.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| workspace_id | object.id | Stable workspace identifier within the organization. |
| actor_id | user.id | Subject that requested the workspace transition. |
| revision | object.version | Snapshot observed when workspace.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Membership events

Index `principal_id` as a membership-specific attribute. Pair it with organization_id when comparing records across workspaces.

### membership.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| membership_id | object.id | Stable membership identifier within the organization. |
| actor_id | user.id | Subject that requested the membership transition. |
| revision | object.version | Snapshot observed when membership.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### membership.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| membership_id | object.id | Stable membership identifier within the organization. |
| actor_id | user.id | Subject that requested the membership transition. |
| revision | object.version | Snapshot observed when membership.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### membership.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| membership_id | object.id | Stable membership identifier within the organization. |
| actor_id | user.id | Subject that requested the membership transition. |
| revision | object.version | Snapshot observed when membership.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### membership.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| membership_id | object.id | Stable membership identifier within the organization. |
| actor_id | user.id | Subject that requested the membership transition. |
| revision | object.version | Snapshot observed when membership.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Role events

Index `role_name` as a role-specific attribute. Pair it with organization_id when comparing records across workspaces.

### role.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| role_id | object.id | Stable role identifier within the organization. |
| actor_id | user.id | Subject that requested the role transition. |
| revision | object.version | Snapshot observed when role.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### role.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| role_id | object.id | Stable role identifier within the organization. |
| actor_id | user.id | Subject that requested the role transition. |
| revision | object.version | Snapshot observed when role.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### role.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| role_id | object.id | Stable role identifier within the organization. |
| actor_id | user.id | Subject that requested the role transition. |
| revision | object.version | Snapshot observed when role.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### role.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| role_id | object.id | Stable role identifier within the organization. |
| actor_id | user.id | Subject that requested the role transition. |
| revision | object.version | Snapshot observed when role.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Grant events

Index `capability` as a grant-specific attribute. Pair it with organization_id when comparing records across workspaces.

### grant.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| grant_id | object.id | Stable grant identifier within the organization. |
| actor_id | user.id | Subject that requested the grant transition. |
| revision | object.version | Snapshot observed when grant.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### grant.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| grant_id | object.id | Stable grant identifier within the organization. |
| actor_id | user.id | Subject that requested the grant transition. |
| revision | object.version | Snapshot observed when grant.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### grant.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| grant_id | object.id | Stable grant identifier within the organization. |
| actor_id | user.id | Subject that requested the grant transition. |
| revision | object.version | Snapshot observed when grant.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### grant.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| grant_id | object.id | Stable grant identifier within the organization. |
| actor_id | user.id | Subject that requested the grant transition. |
| revision | object.version | Snapshot observed when grant.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Identity events

Index `issuer` as a identity-specific attribute. Pair it with organization_id when comparing records across workspaces.

### identity.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| identity_id | object.id | Stable identity identifier within the organization. |
| actor_id | user.id | Subject that requested the identity transition. |
| revision | object.version | Snapshot observed when identity.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### identity.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| identity_id | object.id | Stable identity identifier within the organization. |
| actor_id | user.id | Subject that requested the identity transition. |
| revision | object.version | Snapshot observed when identity.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### identity.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| identity_id | object.id | Stable identity identifier within the organization. |
| actor_id | user.id | Subject that requested the identity transition. |
| revision | object.version | Snapshot observed when identity.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### identity.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| identity_id | object.id | Stable identity identifier within the organization. |
| actor_id | user.id | Subject that requested the identity transition. |
| revision | object.version | Snapshot observed when identity.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Credential events

Index `key_id` as a credential-specific attribute. Pair it with organization_id when comparing records across workspaces.

### credential.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| credential_id | object.id | Stable credential identifier within the organization. |
| actor_id | user.id | Subject that requested the credential transition. |
| revision | object.version | Snapshot observed when credential.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### credential.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| credential_id | object.id | Stable credential identifier within the organization. |
| actor_id | user.id | Subject that requested the credential transition. |
| revision | object.version | Snapshot observed when credential.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### credential.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| credential_id | object.id | Stable credential identifier within the organization. |
| actor_id | user.id | Subject that requested the credential transition. |
| revision | object.version | Snapshot observed when credential.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### credential.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| credential_id | object.id | Stable credential identifier within the organization. |
| actor_id | user.id | Subject that requested the credential transition. |
| revision | object.version | Snapshot observed when credential.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Export events

Index `export_cursor` as a export-specific attribute. Pair it with organization_id when comparing records across workspaces.

### export.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| export_id | object.id | Stable export identifier within the organization. |
| actor_id | user.id | Subject that requested the export transition. |
| revision | object.version | Snapshot observed when export.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### export.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| export_id | object.id | Stable export identifier within the organization. |
| actor_id | user.id | Subject that requested the export transition. |
| revision | object.version | Snapshot observed when export.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### export.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| export_id | object.id | Stable export identifier within the organization. |
| actor_id | user.id | Subject that requested the export transition. |
| revision | object.version | Snapshot observed when export.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### export.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| export_id | object.id | Stable export identifier within the organization. |
| actor_id | user.id | Subject that requested the export transition. |
| revision | object.version | Snapshot observed when export.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Archive events

Index `archive_digest` as a archive-specific attribute. Pair it with organization_id when comparing records across workspaces.

### archive.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| archive_id | object.id | Stable archive identifier within the organization. |
| actor_id | user.id | Subject that requested the archive transition. |
| revision | object.version | Snapshot observed when archive.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### archive.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| archive_id | object.id | Stable archive identifier within the organization. |
| actor_id | user.id | Subject that requested the archive transition. |
| revision | object.version | Snapshot observed when archive.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### archive.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| archive_id | object.id | Stable archive identifier within the organization. |
| actor_id | user.id | Subject that requested the archive transition. |
| revision | object.version | Snapshot observed when archive.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### archive.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| archive_id | object.id | Stable archive identifier within the organization. |
| actor_id | user.id | Subject that requested the archive transition. |
| revision | object.version | Snapshot observed when archive.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Retention events

Index `expires_at` as a retention-specific attribute. Pair it with organization_id when comparing records across workspaces.

### retention.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| retention_id | object.id | Stable retention identifier within the organization. |
| actor_id | user.id | Subject that requested the retention transition. |
| revision | object.version | Snapshot observed when retention.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### retention.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| retention_id | object.id | Stable retention identifier within the organization. |
| actor_id | user.id | Subject that requested the retention transition. |
| revision | object.version | Snapshot observed when retention.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### retention.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| retention_id | object.id | Stable retention identifier within the organization. |
| actor_id | user.id | Subject that requested the retention transition. |
| revision | object.version | Snapshot observed when retention.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### retention.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| retention_id | object.id | Stable retention identifier within the organization. |
| actor_id | user.id | Subject that requested the retention transition. |
| revision | object.version | Snapshot observed when retention.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Cursor events

Index `next_offset` as a cursor-specific attribute. Pair it with organization_id when comparing records across workspaces.

### cursor.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| cursor_id | object.id | Stable cursor identifier within the organization. |
| actor_id | user.id | Subject that requested the cursor transition. |
| revision | object.version | Snapshot observed when cursor.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### cursor.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| cursor_id | object.id | Stable cursor identifier within the organization. |
| actor_id | user.id | Subject that requested the cursor transition. |
| revision | object.version | Snapshot observed when cursor.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### cursor.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| cursor_id | object.id | Stable cursor identifier within the organization. |
| actor_id | user.id | Subject that requested the cursor transition. |
| revision | object.version | Snapshot observed when cursor.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### cursor.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| cursor_id | object.id | Stable cursor identifier within the organization. |
| actor_id | user.id | Subject that requested the cursor transition. |
| revision | object.version | Snapshot observed when cursor.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Receipt events

Index `decision_id` as a receipt-specific attribute. Pair it with organization_id when comparing records across workspaces.

### receipt.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| receipt_id | object.id | Stable receipt identifier within the organization. |
| actor_id | user.id | Subject that requested the receipt transition. |
| revision | object.version | Snapshot observed when receipt.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### receipt.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| receipt_id | object.id | Stable receipt identifier within the organization. |
| actor_id | user.id | Subject that requested the receipt transition. |
| revision | object.version | Snapshot observed when receipt.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### receipt.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| receipt_id | object.id | Stable receipt identifier within the organization. |
| actor_id | user.id | Subject that requested the receipt transition. |
| revision | object.version | Snapshot observed when receipt.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### receipt.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| receipt_id | object.id | Stable receipt identifier within the organization. |
| actor_id | user.id | Subject that requested the receipt transition. |
| revision | object.version | Snapshot observed when receipt.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Revision events

Index `parent_revision` as a revision-specific attribute. Pair it with organization_id when comparing records across workspaces.

### revision.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| revision_id | object.id | Stable revision identifier within the organization. |
| actor_id | user.id | Subject that requested the revision transition. |
| revision | object.version | Snapshot observed when revision.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### revision.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| revision_id | object.id | Stable revision identifier within the organization. |
| actor_id | user.id | Subject that requested the revision transition. |
| revision | object.version | Snapshot observed when revision.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### revision.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| revision_id | object.id | Stable revision identifier within the organization. |
| actor_id | user.id | Subject that requested the revision transition. |
| revision | object.version | Snapshot observed when revision.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### revision.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| revision_id | object.id | Stable revision identifier within the organization. |
| actor_id | user.id | Subject that requested the revision transition. |
| revision | object.version | Snapshot observed when revision.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Manifest events

Index `source_path` as a manifest-specific attribute. Pair it with organization_id when comparing records across workspaces.

### manifest.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| manifest_id | object.id | Stable manifest identifier within the organization. |
| actor_id | user.id | Subject that requested the manifest transition. |
| revision | object.version | Snapshot observed when manifest.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### manifest.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| manifest_id | object.id | Stable manifest identifier within the organization. |
| actor_id | user.id | Subject that requested the manifest transition. |
| revision | object.version | Snapshot observed when manifest.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### manifest.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| manifest_id | object.id | Stable manifest identifier within the organization. |
| actor_id | user.id | Subject that requested the manifest transition. |
| revision | object.version | Snapshot observed when manifest.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### manifest.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| manifest_id | object.id | Stable manifest identifier within the organization. |
| actor_id | user.id | Subject that requested the manifest transition. |
| revision | object.version | Snapshot observed when manifest.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Plan events

Index `base_revision` as a plan-specific attribute. Pair it with organization_id when comparing records across workspaces.

### plan.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| plan_id | object.id | Stable plan identifier within the organization. |
| actor_id | user.id | Subject that requested the plan transition. |
| revision | object.version | Snapshot observed when plan.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### plan.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| plan_id | object.id | Stable plan identifier within the organization. |
| actor_id | user.id | Subject that requested the plan transition. |
| revision | object.version | Snapshot observed when plan.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### plan.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| plan_id | object.id | Stable plan identifier within the organization. |
| actor_id | user.id | Subject that requested the plan transition. |
| revision | object.version | Snapshot observed when plan.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### plan.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| plan_id | object.id | Stable plan identifier within the organization. |
| actor_id | user.id | Subject that requested the plan transition. |
| revision | object.version | Snapshot observed when plan.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Deployment events

Index `environment` as a deployment-specific attribute. Pair it with organization_id when comparing records across workspaces.

### deployment.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| deployment_id | object.id | Stable deployment identifier within the organization. |
| actor_id | user.id | Subject that requested the deployment transition. |
| revision | object.version | Snapshot observed when deployment.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### deployment.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| deployment_id | object.id | Stable deployment identifier within the organization. |
| actor_id | user.id | Subject that requested the deployment transition. |
| revision | object.version | Snapshot observed when deployment.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### deployment.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| deployment_id | object.id | Stable deployment identifier within the organization. |
| actor_id | user.id | Subject that requested the deployment transition. |
| revision | object.version | Snapshot observed when deployment.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### deployment.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| deployment_id | object.id | Stable deployment identifier within the organization. |
| actor_id | user.id | Subject that requested the deployment transition. |
| revision | object.version | Snapshot observed when deployment.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Promotion events

Index `target_stage` as a promotion-specific attribute. Pair it with organization_id when comparing records across workspaces.

### promotion.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| promotion_id | object.id | Stable promotion identifier within the organization. |
| actor_id | user.id | Subject that requested the promotion transition. |
| revision | object.version | Snapshot observed when promotion.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### promotion.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| promotion_id | object.id | Stable promotion identifier within the organization. |
| actor_id | user.id | Subject that requested the promotion transition. |
| revision | object.version | Snapshot observed when promotion.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### promotion.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| promotion_id | object.id | Stable promotion identifier within the organization. |
| actor_id | user.id | Subject that requested the promotion transition. |
| revision | object.version | Snapshot observed when promotion.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### promotion.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| promotion_id | object.id | Stable promotion identifier within the organization. |
| actor_id | user.id | Subject that requested the promotion transition. |
| revision | object.version | Snapshot observed when promotion.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Rollback events

Index `restore_revision` as a rollback-specific attribute. Pair it with organization_id when comparing records across workspaces.

### rollback.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| rollback_id | object.id | Stable rollback identifier within the organization. |
| actor_id | user.id | Subject that requested the rollback transition. |
| revision | object.version | Snapshot observed when rollback.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### rollback.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| rollback_id | object.id | Stable rollback identifier within the organization. |
| actor_id | user.id | Subject that requested the rollback transition. |
| revision | object.version | Snapshot observed when rollback.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### rollback.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| rollback_id | object.id | Stable rollback identifier within the organization. |
| actor_id | user.id | Subject that requested the rollback transition. |
| revision | object.version | Snapshot observed when rollback.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### rollback.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| rollback_id | object.id | Stable rollback identifier within the organization. |
| actor_id | user.id | Subject that requested the rollback transition. |
| revision | object.version | Snapshot observed when rollback.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Fixture events

Index `case_id` as a fixture-specific attribute. Pair it with organization_id when comparing records across workspaces.

### fixture.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| fixture_id | object.id | Stable fixture identifier within the organization. |
| actor_id | user.id | Subject that requested the fixture transition. |
| revision | object.version | Snapshot observed when fixture.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### fixture.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| fixture_id | object.id | Stable fixture identifier within the organization. |
| actor_id | user.id | Subject that requested the fixture transition. |
| revision | object.version | Snapshot observed when fixture.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### fixture.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| fixture_id | object.id | Stable fixture identifier within the organization. |
| actor_id | user.id | Subject that requested the fixture transition. |
| revision | object.version | Snapshot observed when fixture.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### fixture.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| fixture_id | object.id | Stable fixture identifier within the organization. |
| actor_id | user.id | Subject that requested the fixture transition. |
| revision | object.version | Snapshot observed when fixture.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Replay events

Index `original_trace` as a replay-specific attribute. Pair it with organization_id when comparing records across workspaces.

### replay.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| replay_id | object.id | Stable replay identifier within the organization. |
| actor_id | user.id | Subject that requested the replay transition. |
| revision | object.version | Snapshot observed when replay.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### replay.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| replay_id | object.id | Stable replay identifier within the organization. |
| actor_id | user.id | Subject that requested the replay transition. |
| revision | object.version | Snapshot observed when replay.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### replay.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| replay_id | object.id | Stable replay identifier within the organization. |
| actor_id | user.id | Subject that requested the replay transition. |
| revision | object.version | Snapshot observed when replay.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### replay.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| replay_id | object.id | Stable replay identifier within the organization. |
| actor_id | user.id | Subject that requested the replay transition. |
| revision | object.version | Snapshot observed when replay.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Quota events

Index `limit_value` as a quota-specific attribute. Pair it with organization_id when comparing records across workspaces.

### quota.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| quota_id | object.id | Stable quota identifier within the organization. |
| actor_id | user.id | Subject that requested the quota transition. |
| revision | object.version | Snapshot observed when quota.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### quota.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| quota_id | object.id | Stable quota identifier within the organization. |
| actor_id | user.id | Subject that requested the quota transition. |
| revision | object.version | Snapshot observed when quota.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### quota.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| quota_id | object.id | Stable quota identifier within the organization. |
| actor_id | user.id | Subject that requested the quota transition. |
| revision | object.version | Snapshot observed when quota.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### quota.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| quota_id | object.id | Stable quota identifier within the organization. |
| actor_id | user.id | Subject that requested the quota transition. |
| revision | object.version | Snapshot observed when quota.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Budget events

Index `consumed_units` as a budget-specific attribute. Pair it with organization_id when comparing records across workspaces.

### budget.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| budget_id | object.id | Stable budget identifier within the organization. |
| actor_id | user.id | Subject that requested the budget transition. |
| revision | object.version | Snapshot observed when budget.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### budget.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| budget_id | object.id | Stable budget identifier within the organization. |
| actor_id | user.id | Subject that requested the budget transition. |
| revision | object.version | Snapshot observed when budget.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### budget.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| budget_id | object.id | Stable budget identifier within the organization. |
| actor_id | user.id | Subject that requested the budget transition. |
| revision | object.version | Snapshot observed when budget.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### budget.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| budget_id | object.id | Stable budget identifier within the organization. |
| actor_id | user.id | Subject that requested the budget transition. |
| revision | object.version | Snapshot observed when budget.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Adapter events

Index `provider` as a adapter-specific attribute. Pair it with organization_id when comparing records across workspaces.

### adapter.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| adapter_id | object.id | Stable adapter identifier within the organization. |
| actor_id | user.id | Subject that requested the adapter transition. |
| revision | object.version | Snapshot observed when adapter.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### adapter.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| adapter_id | object.id | Stable adapter identifier within the organization. |
| actor_id | user.id | Subject that requested the adapter transition. |
| revision | object.version | Snapshot observed when adapter.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### adapter.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| adapter_id | object.id | Stable adapter identifier within the organization. |
| actor_id | user.id | Subject that requested the adapter transition. |
| revision | object.version | Snapshot observed when adapter.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### adapter.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| adapter_id | object.id | Stable adapter identifier within the organization. |
| actor_id | user.id | Subject that requested the adapter transition. |
| revision | object.version | Snapshot observed when adapter.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Queue events

Index `queue_depth` as a queue-specific attribute. Pair it with organization_id when comparing records across workspaces.

### queue.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| queue_id | object.id | Stable queue identifier within the organization. |
| actor_id | user.id | Subject that requested the queue transition. |
| revision | object.version | Snapshot observed when queue.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### queue.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| queue_id | object.id | Stable queue identifier within the organization. |
| actor_id | user.id | Subject that requested the queue transition. |
| revision | object.version | Snapshot observed when queue.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### queue.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| queue_id | object.id | Stable queue identifier within the organization. |
| actor_id | user.id | Subject that requested the queue transition. |
| revision | object.version | Snapshot observed when queue.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### queue.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| queue_id | object.id | Stable queue identifier within the organization. |
| actor_id | user.id | Subject that requested the queue transition. |
| revision | object.version | Snapshot observed when queue.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Delivery events

Index `attempt_number` as a delivery-specific attribute. Pair it with organization_id when comparing records across workspaces.

### delivery.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| delivery_id | object.id | Stable delivery identifier within the organization. |
| actor_id | user.id | Subject that requested the delivery transition. |
| revision | object.version | Snapshot observed when delivery.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### delivery.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| delivery_id | object.id | Stable delivery identifier within the organization. |
| actor_id | user.id | Subject that requested the delivery transition. |
| revision | object.version | Snapshot observed when delivery.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### delivery.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| delivery_id | object.id | Stable delivery identifier within the organization. |
| actor_id | user.id | Subject that requested the delivery transition. |
| revision | object.version | Snapshot observed when delivery.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### delivery.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| delivery_id | object.id | Stable delivery identifier within the organization. |
| actor_id | user.id | Subject that requested the delivery transition. |
| revision | object.version | Snapshot observed when delivery.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Subscription events

Index `filter` as a subscription-specific attribute. Pair it with organization_id when comparing records across workspaces.

### subscription.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| subscription_id | object.id | Stable subscription identifier within the organization. |
| actor_id | user.id | Subject that requested the subscription transition. |
| revision | object.version | Snapshot observed when subscription.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### subscription.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| subscription_id | object.id | Stable subscription identifier within the organization. |
| actor_id | user.id | Subject that requested the subscription transition. |
| revision | object.version | Snapshot observed when subscription.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### subscription.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| subscription_id | object.id | Stable subscription identifier within the organization. |
| actor_id | user.id | Subject that requested the subscription transition. |
| revision | object.version | Snapshot observed when subscription.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### subscription.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| subscription_id | object.id | Stable subscription identifier within the organization. |
| actor_id | user.id | Subject that requested the subscription transition. |
| revision | object.version | Snapshot observed when subscription.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Route events

Index `route_pattern` as a route-specific attribute. Pair it with organization_id when comparing records across workspaces.

### route.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| route_id | object.id | Stable route identifier within the organization. |
| actor_id | user.id | Subject that requested the route transition. |
| revision | object.version | Snapshot observed when route.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### route.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| route_id | object.id | Stable route identifier within the organization. |
| actor_id | user.id | Subject that requested the route transition. |
| revision | object.version | Snapshot observed when route.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### route.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| route_id | object.id | Stable route identifier within the organization. |
| actor_id | user.id | Subject that requested the route transition. |
| revision | object.version | Snapshot observed when route.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### route.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| route_id | object.id | Stable route identifier within the organization. |
| actor_id | user.id | Subject that requested the route transition. |
| revision | object.version | Snapshot observed when route.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Resolver events

Index `resolver_version` as a resolver-specific attribute. Pair it with organization_id when comparing records across workspaces.

### resolver.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| resolver_id | object.id | Stable resolver identifier within the organization. |
| actor_id | user.id | Subject that requested the resolver transition. |
| revision | object.version | Snapshot observed when resolver.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### resolver.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| resolver_id | object.id | Stable resolver identifier within the organization. |
| actor_id | user.id | Subject that requested the resolver transition. |
| revision | object.version | Snapshot observed when resolver.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### resolver.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| resolver_id | object.id | Stable resolver identifier within the organization. |
| actor_id | user.id | Subject that requested the resolver transition. |
| revision | object.version | Snapshot observed when resolver.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### resolver.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| resolver_id | object.id | Stable resolver identifier within the organization. |
| actor_id | user.id | Subject that requested the resolver transition. |
| revision | object.version | Snapshot observed when resolver.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Cache events

Index `cache_age` as a cache-specific attribute. Pair it with organization_id when comparing records across workspaces.

### cache.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| cache_id | object.id | Stable cache identifier within the organization. |
| actor_id | user.id | Subject that requested the cache transition. |
| revision | object.version | Snapshot observed when cache.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### cache.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| cache_id | object.id | Stable cache identifier within the organization. |
| actor_id | user.id | Subject that requested the cache transition. |
| revision | object.version | Snapshot observed when cache.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### cache.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| cache_id | object.id | Stable cache identifier within the organization. |
| actor_id | user.id | Subject that requested the cache transition. |
| revision | object.version | Snapshot observed when cache.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### cache.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| cache_id | object.id | Stable cache identifier within the organization. |
| actor_id | user.id | Subject that requested the cache transition. |
| revision | object.version | Snapshot observed when cache.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Signature events

Index `algorithm` as a signature-specific attribute. Pair it with organization_id when comparing records across workspaces.

### signature.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| signature_id | object.id | Stable signature identifier within the organization. |
| actor_id | user.id | Subject that requested the signature transition. |
| revision | object.version | Snapshot observed when signature.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### signature.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| signature_id | object.id | Stable signature identifier within the organization. |
| actor_id | user.id | Subject that requested the signature transition. |
| revision | object.version | Snapshot observed when signature.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### signature.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| signature_id | object.id | Stable signature identifier within the organization. |
| actor_id | user.id | Subject that requested the signature transition. |
| revision | object.version | Snapshot observed when signature.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### signature.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| signature_id | object.id | Stable signature identifier within the organization. |
| actor_id | user.id | Subject that requested the signature transition. |
| revision | object.version | Snapshot observed when signature.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Approval events

Index `reviewer` as a approval-specific attribute. Pair it with organization_id when comparing records across workspaces.

### approval.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| approval_id | object.id | Stable approval identifier within the organization. |
| actor_id | user.id | Subject that requested the approval transition. |
| revision | object.version | Snapshot observed when approval.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### approval.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| approval_id | object.id | Stable approval identifier within the organization. |
| actor_id | user.id | Subject that requested the approval transition. |
| revision | object.version | Snapshot observed when approval.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### approval.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| approval_id | object.id | Stable approval identifier within the organization. |
| actor_id | user.id | Subject that requested the approval transition. |
| revision | object.version | Snapshot observed when approval.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### approval.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| approval_id | object.id | Stable approval identifier within the organization. |
| actor_id | user.id | Subject that requested the approval transition. |
| revision | object.version | Snapshot observed when approval.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Exception events

Index `reason` as a exception-specific attribute. Pair it with organization_id when comparing records across workspaces.

### exception.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| exception_id | object.id | Stable exception identifier within the organization. |
| actor_id | user.id | Subject that requested the exception transition. |
| revision | object.version | Snapshot observed when exception.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### exception.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| exception_id | object.id | Stable exception identifier within the organization. |
| actor_id | user.id | Subject that requested the exception transition. |
| revision | object.version | Snapshot observed when exception.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### exception.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| exception_id | object.id | Stable exception identifier within the organization. |
| actor_id | user.id | Subject that requested the exception transition. |
| revision | object.version | Snapshot observed when exception.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### exception.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| exception_id | object.id | Stable exception identifier within the organization. |
| actor_id | user.id | Subject that requested the exception transition. |
| revision | object.version | Snapshot observed when exception.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Scope events

Index `scope_name` as a scope-specific attribute. Pair it with organization_id when comparing records across workspaces.

### scope.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| scope_id | object.id | Stable scope identifier within the organization. |
| actor_id | user.id | Subject that requested the scope transition. |
| revision | object.version | Snapshot observed when scope.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### scope.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| scope_id | object.id | Stable scope identifier within the organization. |
| actor_id | user.id | Subject that requested the scope transition. |
| revision | object.version | Snapshot observed when scope.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### scope.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| scope_id | object.id | Stable scope identifier within the organization. |
| actor_id | user.id | Subject that requested the scope transition. |
| revision | object.version | Snapshot observed when scope.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### scope.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| scope_id | object.id | Stable scope identifier within the organization. |
| actor_id | user.id | Subject that requested the scope transition. |
| revision | object.version | Snapshot observed when scope.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Binding events

Index `subject_id` as a binding-specific attribute. Pair it with organization_id when comparing records across workspaces.

### binding.requested

The service accepted an intent, before validation. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| binding_id | object.id | Stable binding identifier within the organization. |
| actor_id | user.id | Subject that requested the binding transition. |
| revision | object.version | Snapshot observed when binding.requested was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### binding.validated

The validator checked the candidate against the active revision. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| binding_id | object.id | Stable binding identifier within the organization. |
| actor_id | user.id | Subject that requested the binding transition. |
| revision | object.version | Snapshot observed when binding.validated was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### binding.committed

The owning service persisted the state transition. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| binding_id | object.id | Stable binding identifier within the organization. |
| actor_id | user.id | Subject that requested the binding transition. |
| revision | object.version | Snapshot observed when binding.committed was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |

### binding.rejected

The service refused the change. No revision was committed. Correlate the record with the originating request using trace.id. Use event.id for deduplication across delivery retries.

| Payload field | SIEM mapping | Interpretation |
| --- | --- | --- |
| binding_id | object.id | Stable binding identifier within the organization. |
| actor_id | user.id | Subject that requested the binding transition. |
| revision | object.version | Snapshot observed when binding.rejected was recorded. |
| occurred_at | @timestamp | UTC producer timestamp, independent of export arrival. |


## Compliance appendices

Use the hot tier for incident searches during the first 30 days. Archive signed batches for 365 days. A legal hold suspends expiry for the selected organization. Verify the export digest before handing evidence to a reviewer.

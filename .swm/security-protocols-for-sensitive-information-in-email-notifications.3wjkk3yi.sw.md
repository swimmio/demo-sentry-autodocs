---
title: Security Protocols for Sensitive Information in Email Notifications
---
This document will explore the security protocols Sentry employs to protect sensitive information in notifications. Key areas covered include:

1. Enhanced privacy settings in email notifications.
2. Security measures in notification functions across various integrations.

# Enhanced Privacy in Email Notifications

This section of the code explains how Sentry handles sensitive information in email notifications when enhanced privacy settings are enabled. It restricts the details shown in the notification, directing users to view the issue on Sentry's platform for more information.

<SwmSnippet path="/src/sentry/integrations/slack/utils/notifications.py" line="29">

---

# Security Measures in Notification Functions

This function outlines the security checks performed before sending incident alert notifications through Slack. It ensures that the organization integration is active and handles exceptions securely, preventing sensitive information leaks.

```python
def send_incident_alert_notification(
    action: AlertRuleTriggerAction,
    incident: Incident,
    metric_value: float,
    new_status: IncidentStatus,
    notification_uuid: str | None = None,
) -> bool:
    # Make sure organization integration is still active:
    integration, org_integration = integration_service.get_organization_context(
        organization_id=incident.organization_id, integration_id=action.integration_id
    )
    if org_integration is None or integration is None or integration.status != ObjectStatus.ACTIVE:
        # Integration removed, but rule is still active.
        return False

    organization = incident.organization
    chart_url = None
    if features.has("organizations:metric-alert-chartcuterie", incident.organization):
        try:
            chart_url = build_metric_alert_chart(
                organization=organization,
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

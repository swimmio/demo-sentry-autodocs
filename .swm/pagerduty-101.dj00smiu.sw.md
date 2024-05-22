---
title: PagerDuty 101
---
PagerDuty in the Sentry integration context is a service that allows users to manage incidents and outages by sending Sentry notifications to PagerDuty. This integration enables the creation of rule-based alerts that can automatically trigger incidents in one or multiple PagerDuty services directly from Sentry alerts. This helps in streamlining the incident management process and ensures that critical issues are communicated promptly to the right teams within an organization.

<SwmSnippet path="/src/sentry/integrations/pagerduty/client.py" line="36">

---

# PagerDuty Integration Endpoint

The `send_trigger` method in the `PagerDutyClient` class is responsible for sending notifications to PagerDuty. It constructs a payload based on the Sentry event data, which includes details like the event summary, severity, source, and a link to the Sentry issue. This payload is then sent to the PagerDuty API endpoint defined by `base_url`.

```python
    def send_trigger(
        self,
        data,
        notification_uuid: str | None = None,
        severity: PagerdutySeverity | None = None,
    ):
        # expected payload: https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2
        if isinstance(data, (Event, GroupEvent)):
            source = data.transaction or data.culprit or "<unknown>"
            group = data.group
            level = data.get_tag("level") or "error"
            custom_details = serialize(data, None, ExternalEventSerializer())
            summary = custom_details["message"][:1024] or custom_details["title"]
            link_params = {"referrer": "pagerduty_integration"}
            if notification_uuid:
                link_params["notification_uuid"] = notification_uuid

            if severity == PAGERDUTY_DEFAULT_SEVERITY:
                severity = LEVEL_SEVERITY_MAP[level]

            payload = {
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

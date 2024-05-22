---
title: Ensuring Timely Delivery of Notifications in Sentry
---
This document will explore how Sentry ensures the timely delivery of notifications, focusing on:

<SwmSnippet path="/src/sentry/integrations/slack/actions/notification.py" line="244">

---

# Notification Delivery Mechanism

This section of the code in `send_confirmation_notification` function outlines how Sentry sends notifications through Slack. It prepares the notification payload and sends it using the Slack API. The function handles potential API errors and logs them, ensuring that the notification delivery process is monitored and errors are addressed promptly.

```python
    def send_confirmation_notification(
        self, rule: Rule, new: bool, changed: dict[str, Any] | None = None
    ):
        integration = self.get_integration()
        if not integration:
            # Integration removed, rule still active.
            return

        channel = self.get_option("channel_id")
        blocks = SlackRuleSaveEditMessageBuilder(rule=rule, new=new, changed=changed).build()
        payload = {
            "text": blocks.get("text"),
            "blocks": json.dumps_experimental(
                "integrations.slack.enable-orjson", blocks.get("blocks")
            ),
            "channel": channel,
            "unfurl_links": False,
            "unfurl_media": False,
        }
        client = SlackClient(integration_id=integration.id)
        try:
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/api/bases/organization_integrations.py" line="49">

---

# Integration and Configuration Retrieval

The `get_integration` function is crucial for retrieving integration details necessary for sending notifications. It ensures that the integration exists and is correctly linked to the organization, which is a key step in the notification delivery process.

```python
    def get_integration(organization_id: int, integration_id: int) -> Integration:
        """
        Note: The integration may still exist even when the
        OrganizationIntegration cross table entry has been deleted.

        :param organization:
        :param integration_id:
        :return:
        """
        try:
            return Integration.objects.get(
                id=integration_id, organizationintegration__organization_id=organization_id
            )
        except Integration.DoesNotExist:
            raise Http404
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

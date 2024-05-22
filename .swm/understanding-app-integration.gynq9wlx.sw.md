---
title: Understanding App Integration
---
# App Integration

App Integration in Sentry primarily involves the interaction and communication between Sentry and third-party applications through webhooks and other mechanisms. In the `src/sentry/utils/sentry_apps` directory, the code manages the behavior of Sentry Apps, especially focusing on handling webhook requests and errors. For instance, it includes functionalities to buffer requests and monitor errors for each Sentry App, ensuring that any issues with connectivity or timeouts are recorded and addressed. This helps in maintaining the reliability and efficiency of integrations with various applications.

<SwmSnippet path="/src/sentry/utils/sentry_apps/webhooks.py" line="104">

---

# Webhook Endpoints for App Integration

This section of the code defines an endpoint `send_and_save_webhook_request` which is responsible for sending webhook requests to a specified URL and handling the responses. It logs the request and response details in a buffer, checks for timeouts, and records the response status to determine if the integration is broken. This function is crucial for maintaining the reliability and functionality of app integrations within Sentry.

```python
@ignore_unpublished_app_errors
def send_and_save_webhook_request(
    sentry_app: SentryApp | RpcSentryApp,
    app_platform_event: AppPlatformEvent,
    url: str | None = None,
) -> Response:
    """
    Notify a SentryApp's webhook about an incident and log response on redis.

    :param sentry_app: The SentryApp to notify via a webhook.
    :param app_platform_event: Incident data. See AppPlatformEvent.
    :param url: The URL to hit for this webhook if it is different from `sentry_app.webhook_url`.
    :return: Webhook response
    """
    buffer = SentryAppWebhookRequestsBuffer(sentry_app)

    org_id = app_platform_event.install.organization_id
    event = f"{app_platform_event.resource}.{app_platform_event.action}"
    slug = sentry_app.slug_for_metrics
    url = url or sentry_app.webhook_url
    response = None
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

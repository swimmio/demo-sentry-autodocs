---
title: What is App Integration
---
# App Integration

App Integration in Sentry involves connecting third-party applications to extend the functionality of Sentry. Specifically, in the `src/sentry/utils/sentry_apps` directory, the code manages Sentry App webhook requests and error handling. For instance, it includes mechanisms to store information about webhook requests in Redis, ensuring that the last 100 requests and errors are recorded for each event type and Sentry App. This setup helps in monitoring and managing the performance and reliability of integrations with external services.

<SwmSnippet path="/src/sentry/utils/sentry_apps/webhooks.py" line="105">

---

# Endpoints of App Integration

This section of the code defines an endpoint for sending webhook requests to Sentry apps. It handles the request by sending data to the specified URL and logs the response. Errors such as timeouts and connection errors are tracked, and the integration's status may be updated based on the response, indicating whether the integration is broken.

```python
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
    try:
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

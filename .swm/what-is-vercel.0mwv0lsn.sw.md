---
title: What is Vercel
---
# Vercel Integration in Sentry

Vercel is a platform that supports static and JAMstack deployments with global CDN and Serverless Functions. In the Sentry codebase, specifically under `src/sentry/integrations/vercel`, Vercel is integrated to enhance the deployment features of Sentry projects. This integration allows for automatic uploading of source maps and notification of new releases being deployed to Sentry, directly connecting Sentry and Vercel projects. Additionally, the integration facilitates the installation process through the Vercel Marketplace, ensuring a seamless sync between Vercel and Sentry projects.

<SwmSnippet path="/src/sentry/integrations/vercel/urls.py" line="7">

---

# Vercel Integration Endpoints

The file `urls.py` defines three main endpoints for the Vercel integration: `/configure/`, `/delete/`, and `/webhook/`. These endpoints are linked to views that handle configuration, deletion, and webhook events from Vercel respectively.

```python
urlpatterns = [
    re_path(
        r"^configure/$",
        VercelExtensionConfigurationView.as_view(),
        name="sentry-extensions-vercel-configure",
    ),
    # Since we've been endorsing using `/delete` as the endpoint for Self-Hosted, we need to
    # keep it operational for existing integrations. This is purely aesthetic, as both routes
    # will use the same webhook (Previously known as 'Generic Webhook' - See #26185)
    re_path(
        r"^delete/$",
        VercelWebhookEndpoint.as_view(),
        name="sentry-extensions-vercel-delete",
    ),
    re_path(
        r"^webhook/$",
        VercelWebhookEndpoint.as_view(),
        name="sentry-extensions-vercel-webhook",
    ),
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/vercel/webhook.py" line="130">

---

# Webhook Endpoint Handling

The `VercelWebhookEndpoint` class in `webhook.py` handles POST and DELETE requests. It processes webhook events such as deployment creation and integration configuration removal, verifying requests and parsing external IDs from Vercel.

```python
@control_silo_endpoint
class VercelWebhookEndpoint(Endpoint):
    owner = ApiOwner.INTEGRATIONS
    publish_status = {
        "DELETE": ApiPublishStatus.PRIVATE,
        "POST": ApiPublishStatus.PRIVATE,
    }
    authentication_classes = ()
    permission_classes = ()
    provider = "vercel"

    @csrf_exempt
    def dispatch(self, request: Request, *args, **kwargs) -> Response:
        return super().dispatch(request, *args, **kwargs)

    def parse_external_id(self, request: Request) -> str:
        payload = request.data["payload"]
        # New Vercel request flow
        external_id = (
            payload.get("team")["id"]
            if (payload.get("team") and payload.get("team") != {})
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

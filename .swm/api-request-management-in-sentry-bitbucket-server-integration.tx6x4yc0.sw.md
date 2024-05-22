---
title: API Request Management in Sentry-Bitbucket Server Integration
---
This document will explore how API requests are managed between Sentry and Bitbucket Server, focusing on:

# Overview of API Request Management

API requests between Sentry and Bitbucket Server are primarily managed through the integration modules located in `src/sentry/integrations/bitbucket_server/`. These modules handle various aspects of the integration, such as repository management, webhooks, and client API interactions.

<SwmSnippet path="/src/sentry/middleware/integrations/parsers/bitbucket_server.py" line="14">

---

# Handling Webhooks

The `BitbucketServerRequestParser` class is crucial for handling webhook requests from Bitbucket Server. It determines the appropriate response based on the type of webhook received.

```python
class BitbucketServerRequestParser(BitbucketRequestParser):
    provider = "bitbucket_server"
    webhook_identifier = WebhookProviderIdentifier.BITBUCKET_SERVER

    def get_response(self) -> HttpResponseBase:
        if self.view_class == BitbucketServerWebhookEndpoint:
            return self.get_bitbucket_webhook_response()
        return self.get_response_from_control_silo()
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

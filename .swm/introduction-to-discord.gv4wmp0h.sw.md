---
title: Introduction to Discord
---
<SwmSnippet path="/src/sentry/integrations/discord/integration.py" line="28">

---

# Discord Integration in Sentry

Discord is a platform for team communication and collaboration. In Sentry, the Discord integration allows users to connect their Sentry instance with their Discord server. This enables them to receive alerts directly in Discord channels or through direct messages, based on the issues and errors tracked by Sentry. This integration enhances the real-time response capabilities by notifying the team immediately when issues occur.

```python
DESCRIPTION = """Discord’s your place to collaborate, share, and just talk about your day – or
commiserate about app errors. Connect Sentry to your Discord server and get
[alerts](https://docs.sentry.io/product/alerts/alert-types/) in a channel of your choice or via
direct message when sh%t hits the fan."""
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/discord/webhooks/base.py" line="24">

---

# Discord Interactions Endpoint

This section of the code defines the `DiscordInteractionsEndpoint` class, which is crucial for handling incoming HTTP POST requests from Discord. It determines the type of interaction (ping, command, or message component) and routes the request to the appropriate handler. This endpoint is essential for the integration as it processes all Discord interactions with Sentry.

```python
@all_silo_endpoint
class DiscordInteractionsEndpoint(Endpoint):
    owner = ApiOwner.INTEGRATIONS
    publish_status = {
        "POST": ApiPublishStatus.UNKNOWN,
    }
    """
    All Discord -> Sentry communication will come through our interactions
    endpoint. We need to figure out what Discord is sending us and direct the
    request to the appropriate handler.
    """

    authentication_classes = ()
    permission_classes = ()
    discord_request_class = DiscordRequest
    provider = "discord"

    def __init__(self) -> None:
        super().__init__()

    @classmethod
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

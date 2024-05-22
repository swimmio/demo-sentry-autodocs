---
title: Getting started with MS Teams
---
# MS Teams Integration in Sentry

Microsoft Teams, often referred to as MS Teams, is a hub for teamwork in Office 365, integrating chats, meetings, files, and apps in a single place. In the context of Sentry, MS Teams is leveraged to enhance collaboration and incident management within software teams. Sentry's integration with MS Teams allows users to receive alerts directly in their Teams channels. These alerts can be interacted with to assign, ignore, or resolve issues directly from the chat interface. Additionally, Sentry supports configuring rule-based alerts that can automatically post notifications to specific Teams channels or users, streamlining the workflow for monitoring and reacting to issues in real-time.

<SwmSnippet path="/src/sentry/integrations/msteams/client.py" line="22">

---

# MS Teams Client API

This section of the code defines various endpoints for interacting with MS Teams, such as fetching team info, channel lists, and sending messages or cards. The `MsTeamsClientMixin` class provides methods like `get_team_info`, `get_channel_list`, and `send_message` which utilize the MS Teams API endpoints.

```python
class MsTeamsClientMixin:
    integration_name = "msteams"
    TEAM_URL = "/v3/teams/%s"
    CHANNEL_URL = "/v3/teams/%s/conversations"
    ACTIVITY_URL = "/v3/conversations/%s/activities"
    MESSAGE_URL = "/v3/conversations/%s/activities/%s"
    CONVERSATION_URL = "/v3/conversations"
    MEMBER_URL = "/v3/conversations/%s/pagedmembers"

    def get_team_info(self, team_id: str):
        return self.get(self.TEAM_URL % team_id)

    def get_channel_list(self, team_id: str):
        resp = self.get(self.CHANNEL_URL % team_id)
        return resp.get("conversations")

    def get_member_list(self, team_id: str, continuation_token: str | None = None):
        url = self.MEMBER_URL % team_id
        params = {"pageSize": 500}
        if continuation_token:
            params["continuationToken"] = continuation_token
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/msteams/webhook.py" line="235">

---

# MS Teams Webhook Handling

This section handles incoming webhook requests from MS Teams. The `MsTeamsWebhookEndpoint` class processes different types of events such as installation updates, messages, and conversation updates. It uses methods like `handle_installation_update_event` and `handle_message_event` to manage the data received from MS Teams.

```python
class MsTeamsWebhookEndpoint(Endpoint, MsTeamsWebhookMixin):
    owner = ApiOwner.INTEGRATIONS
    publish_status = {
        "POST": ApiPublishStatus.PRIVATE,
    }
    authentication_classes = ()
    permission_classes = ()
    provider = "msteams"

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self._event_handlers: dict[MsTeamsEvents, Callable[[HttpRequest], HttpResponse]] = {
            MsTeamsEvents.MESSAGE: self.handle_message_event,
            MsTeamsEvents.CONVERSATION_UPDATE: self.handle_conversation_update_event,
            MsTeamsEvents.INSTALLATION_UPDATE: self.handle_installation_update_event,
            MsTeamsEvents.UNKNOWN: self.handle_unknown_event,
        }

    @csrf_exempt
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

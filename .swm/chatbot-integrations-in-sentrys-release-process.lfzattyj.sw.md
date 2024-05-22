---
title: Chatbot Integrations in Sentrys Release Process
---
This document will explore the chatbot integrations used in Sentry's release process, focusing on:

# Overview of Chatbot Integrations

Sentry utilizes various chatbot integrations to streamline its release process. These integrations primarily include Discord and Microsoft Teams, which facilitate communication and notifications related to release activities.

<SwmSnippet path="/src/sentry/middleware/integrations/parsers/discord.py" line="18">

---

# Discord Integration

The Discord integration in Sentry is handled through middleware that parses incoming data and interacts with Sentry's internal tasks and models. This integration is crucial for automating responses and managing release notifications efficiently.

```python
)
from sentry.middleware.integrations.tasks import convert_to_async_discord_response
from sentry.models.integrations import Integration
from sentry.models.integrations.organization_integration import OrganizationIntegration
from sentry.models.outbox import WebhookProviderIdentifier
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/msteams/notifications.py" line="9">

---

# Microsoft Teams Integration

Microsoft Teams integration is managed through utilities that help in building adaptive cards and fetching user conversation IDs. This setup is used to send targeted notifications to team members about releases, ensuring that all stakeholders are informed in real time.

```python
from sentry.integrations.msteams.card_builder.block import AdaptiveCard
from sentry.integrations.msteams.utils import get_user_conversation_id
from sentry.integrations.notifications import get_context, get_integrations_by_channel_by_recipient
from sentry.models.team import Team
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

---
title: Management of Rate Limits and Queuing in Email Notifications
---
This document will explore how Sentry handles rate limits and queuing for email notifications to prevent system overloads. We'll cover:

1. How rate limits are configured for email notifications.
2. The queuing mechanism for handling email notifications efficiently.

<SwmSnippet path="/src/sentry/api/endpoints/user_emails_confirm.py" line="43">

---

# Rate Limit Configuration

Rate limits for email notifications are defined here, specifying the limit and the window of time in which this limit applies. This helps in preventing system overloads by controlling the flow of outgoing emails.

```python
        "POST": {
            RateLimitCategory.USER: RateLimit(limit=10, window=60),
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

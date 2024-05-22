---
title: Expiration and Renewal Policies for API Tokens in Sentry
---
This document will cover the policies regarding the expiration and renewal of API tokens in Sentry, focusing on:

<SwmSnippet path="/src/sentry/models/apitoken.py" line="30">

---

# API Token Expiration

API tokens in Sentry have a default expiration time set by the `default_expiration` function, which adds a timedelta of 30 days to the current time. This is defined by the `DEFAULT_EXPIRATION` constant.

```python
def default_expiration():
    return timezone.now() + DEFAULT_EXPIRATION
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

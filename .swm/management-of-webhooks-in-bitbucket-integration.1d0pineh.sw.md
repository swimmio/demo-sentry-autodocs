---
title: Management of Webhooks in Bitbucket Integration
---
This document will explore how webhooks are managed within the Bitbucket integration in Sentry. We'll cover:

1. How webhooks are configured and utilized.
2. The role of scopes in managing webhooks.

<SwmSnippet path="/src/sentry/integrations/bitbucket/integration.py" line="124">

---

# Webhook Management in Bitbucket Integration

Webhooks are managed by checking access to repositories. The `get_hooks` method from `BitbucketApiClient` is called to fetch existing webhooks for a repository. If the repository is accessible and webhooks can be fetched, it returns `True`, otherwise `False` in case of an `ApiError`. This is crucial for managing webhooks effectively within the Bitbucket integration.

```python
        client = self.get_client()
        try:
            client.get_hooks(repo.config["name"])
        except ApiError:
            return False
        return True
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

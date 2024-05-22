---
title: Understanding OAuth Authentication in Bitbucket Integration
---
This document will cover the OAuth authentication process specifically for the Bitbucket integration in Sentry. We'll explore:

1. How OAuth credentials are configured for Bitbucket integration.
2. The role of OAuth in the Bitbucket integration features.

# OAuth Configuration for Bitbucket

To set up OAuth authentication for Bitbucket in Sentry, you need to create an OAuth consumer key and secret in your Bitbucket account and configure these in Sentry. This involves navigating to your Bitbucket API settings, creating the OAuth credentials, and then adding `BITBUCKET_CONSUMER_KEY` and `BITBUCKET_CONSUMER_SECRET` in your Sentry configuration.

<SwmSnippet path="/src/sentry/integrations/bitbucket/integration.py" line="86">

---

# Utilizing OAuth in Bitbucket Integration

The `BitbucketIntegration` class utilizes the OAuth tokens to authenticate API requests. The `get_client` method returns an instance of `BitbucketApiClient` initialized with the OAuth credentials, enabling interactions with the Bitbucket API for various integration features like repository access and issue tracking.

```python
class BitbucketIntegration(IntegrationInstallation, BitbucketIssueBasicMixin, RepositoryMixin):
    repo_search = True

    def get_client(self):
        return BitbucketApiClient(integration=self.model)
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

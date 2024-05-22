---
title: Handling Token Refresh in App Store Connect Integration
---
This document will explain the process for handling token refresh with App Store Connect, focusing on the following aspects:

1. How the token refresh process is initiated
2. The validation and creation of new tokens

<SwmSnippet path="/src/sentry/identity/vsts/provider.py" line="52">

---

# Token Refresh Process Initiation

The token refresh process is initiated by obtaining the refresh token URL, which is used to make a request for a new access token. This is handled by the `get_refresh_token_url` method.

```python
    def get_refresh_token_url(self):
        return self.oauth_access_token_url
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/mediators/token_exchange/refresher.py" line="29">

---

# Token Validation and Creation

The `Refresher` class handles the validation and creation of new tokens. It first validates the existing token, deletes it, and then creates a new token with updated expiration. This process ensures that the token associated with the user and application remains secure and up-to-date.

```python
    def call(self):
        self._validate()
        self._delete_token()
        return self._create_new_token()

    def record_analytics(self):
        analytics.record(
            "sentry_app.token_exchanged",
            sentry_app_installation_id=self.install.id,
            exchange_type="refresh",
        )

    def _validate(self):
        Validator.run(install=self.install, client_id=self.client_id, user=self.user)

        self._validate_token_belongs_to_app()

    def _validate_token_belongs_to_app(self):
        if self.token.application != self.application:
            raise APIUnauthorized

```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

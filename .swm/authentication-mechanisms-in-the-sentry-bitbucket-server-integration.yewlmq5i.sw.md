---
title: Authentication Mechanisms in the Sentry-Bitbucket Server Integration
---
This document will explore the authentication mechanisms used between Sentry and Bitbucket Server, focusing on:

<SwmSnippet path="/src/social_auth/backends/bitbucket.py" line="68">

---

# OAuth Authentication

The `BitbucketAuth` class in `src/social_auth/backends/bitbucket.py` implements the OAuth authentication mechanism. It uses OAuth1 protocol, handling the authorization, request token, and access token URLs to authenticate users and integrate with Bitbucket Server.

```python
class BitbucketAuth(BaseOAuth1):
    """Bitbucket OAuth authentication mechanism"""

    AUTHORIZATION_URL = BITBUCKET_AUTHORIZATION_URL
    REQUEST_TOKEN_URL = BITBUCKET_REQUEST_TOKEN_URL
    ACCESS_TOKEN_URL = BITBUCKET_ACCESS_TOKEN_URL
    AUTH_BACKEND = BitbucketBackend
    SETTINGS_KEY_NAME = "BITBUCKET_CONSUMER_KEY"
    SETTINGS_SECRET_NAME = "BITBUCKET_CONSUMER_SECRET"
    DEFAULT_SCOPE = ["webhook", "repository", "issue"]

    def user_data(self, access_token):
        """Return user data provided"""
        # Bitbucket has a bit of an indirect route to obtain user data from an
        # authenticated query: First obtain the user's email via an
        # authenticated GET
        url = BITBUCKET_EMAIL_DATA_URL
        request = self.oauth_request(access_token, url)
        response = self.fetch_response(request)
        try:
            email = None
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/templates/sentry/integrations/bitbucket-server-config.html" line="26">

---

# Webhook Configuration

The HTML template at `src/sentry/templates/sentry/integrations/bitbucket-server-config.html` provides a user interface for configuring the Bitbucket Server integration in Sentry. It guides users through connecting Sentry with their Bitbucket Server App by adding credentials and completing necessary steps on the Bitbucket Server side.

```html
{% block title %} {% trans "Bitbucket-Server Setup" %} | {{ block.super }} {% endblock %}

{% block main %}
<h3>{% trans "Connect Sentry with your App" %}</h3>
  <p>{% trans "Add your Bitbucket Server App credentials to Sentry." %}</p>
  <p class="alert alert-block flex">
    <i class="icon icon-exclamation"></i>
    <span>
        {% blocktrans %}
        You must complete the <a href="https://docs.sentry.io/product/integrations/source-code-mgmt/bitbucket/#bitbucket-server">required steps</a>

        in Bitbucket Server before attempting to connect with Sentry.
        {% endblocktrans %}
    </span>
  </p>
  <form action="" method="post" class="form-stacked">
    {% csrf_token %}
    <input type="hidden" name="provider" value="bitbucket_server" />

    {{ form|as_crispy_errors }}

```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

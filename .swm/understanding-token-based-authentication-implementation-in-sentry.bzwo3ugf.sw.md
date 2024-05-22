---
title: Understanding Token-Based Authentication Implementation in Sentry
---
This document will cover the implementation of token-based authentication in Sentry, focusing on the following aspects:

1. How tokens are generated and hashed
2. The authentication process using tokens

<SwmSnippet path="/src/sentry/utils/security/orgauthtoken_token.py" line="30">

---

# Token Generation and Hashing

Token generation and hashing are crucial for security. The `generate_token` function creates a new token, and `hash_token` securely hashes the token for storage and comparison.

```python
    json_str = json.dumps(payload)
    payload_encoded = base64_encode_str(json_str)

```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/api/authentication.py" line="14">

---

# Token-Based Authentication Process

The `OrgAuthTokenAuthentication` class handles the authentication of requests using organization auth tokens. It verifies the token against stored hashed tokens to authenticate users.

```python
    BasicAuthentication,
    SessionAuthentication,
    get_authorization_header,
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

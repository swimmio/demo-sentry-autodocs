---
title: Generation and Security Measures of API Tokens in Sentry
---
This document will explore the generation of API tokens within Sentry and the security measures implemented during their creation. Key points include:

1. How API tokens are generated.
2. Security measures in place during token generation.

<SwmSnippet path="/src/sentry/models/apiapplication.py" line="27">

---

# How API Tokens are Generated

API tokens are generated using the `generate_token` function, which utilizes Python's `secrets.token_hex` to create a secure 128-bit token. This ensures that each token is unique and difficult to predict.

```python
def generate_token():
    # `client_id` on `ApiApplication` is currently limited to 64 characters
    # so we need to restrict the length of the secret
    return secrets.token_hex(nbytes=32)  # generates a 128-bit secure token
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

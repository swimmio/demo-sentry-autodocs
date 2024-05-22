---
title: Implementing Secure Storage for Apple API Keys in Sentry
---
This document will cover the secure storage of Apple API keys in Sentry, focusing on:

# Overview of Secure Storage for Apple API Keys

Sentry securely stores Apple API keys to ensure that sensitive data is protected. This involves generating secure keys, managing their lifecycle, and ensuring that they are stored securely in the database.

<SwmSnippet path="/src/sentry/models/apikey.py" line="63">

---

# Key Generation and Storage

Secure API keys are generated using the `generate_api_key` method, which utilizes the `secrets.token_hex` function to create a 16-byte hexadecimal token. This method ensures that each key is unique and secure.

```python
    @classmethod
    def generate_api_key(cls):
        return secrets.token_hex(nbytes=16)
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

---
title: Error Handling Strategies in Bitbucket Integration
---
This document will explore the error handling strategies employed in the Bitbucket integration within Sentry. Key points include:

1. How errors are detected and reported.
2. Strategies to handle API errors during repository access.

<SwmSnippet path="/src/sentry/integrations/bitbucket/integration.py" line="96">

---

# Error Detection and Reporting

Errors from the Bitbucket API are processed by the `error_message_from_json` method, which extracts the error message from the JSON response. This method is crucial for understanding what went wrong during an API request.

```python
    def error_message_from_json(self, data):
        return data.get("error", {}).get("message", "unknown error")
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/bitbucket/integration.py" line="125">

---

# Handling API Errors

The `has_repo_access` method demonstrates error handling by trying to fetch repository hooks and gracefully handling `ApiError` if it occurs. This ensures that the integration does not break and provides a fallback mechanism by returning `False` when an error is encountered.

```python
        try:
            client.get_hooks(repo.config["name"])
        except ApiError:
            return False
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

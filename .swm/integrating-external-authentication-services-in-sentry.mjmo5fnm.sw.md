---
title: Integrating External Authentication Services in Sentry
---
This document will cover how Sentry integrates with external authentication services, focusing on:

# Overview of External Authentication Integration

Sentry integrates with various external authentication services to enhance user identity verification and management. This integration is facilitated through the use of external user mappings and authentication tokens, which help link Sentry's internal user identities with those from external providers like GitHub, Slack, or custom providers.

<SwmSnippet path="/src/sentry/integrations/base.py" line="383">

---

# Code Implementation

The `get_default_identity` function is crucial for fetching the identity associated with an external authentication service. It checks if the default authentication ID is set for an organization integration and retrieves the corresponding identity. This function is used across various integration setups like Bitbucket, VSTS, and GitLab, indicating its central role in handling external authentication.

```python
    def get_default_identity(self) -> RpcIdentity:
        """For Integrations that rely solely on user auth for authentication."""
        if self.org_integration is None or self.org_integration.default_auth_id is None:
            raise Identity.DoesNotExist
        identity = identity_service.get_identity(
            filter={"id": self.org_integration.default_auth_id}
        )
        if identity is None:
            with configure_scope() as scope:
                scope.set_tag("integration_provider", self.model.get_provider().name)
                scope.set_tag("org_integration_id", self.org_integration.id)
                scope.set_tag("default_auth_id", self.org_integration.default_auth_id)
            raise Identity.DoesNotExist
        return identity
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

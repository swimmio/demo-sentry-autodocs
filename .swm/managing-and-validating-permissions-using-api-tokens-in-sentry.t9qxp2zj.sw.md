---
title: Managing and Validating Permissions Using API Tokens in Sentry
---
This document will explore how permissions are managed and validated through API Tokens in Sentry. Key areas covered include:

1. The role of API Tokens in permission management.
2. The validation process of API Tokens.

<SwmSnippet path="/src/sentry/api/endpoints/api_tokens.py" line="31">

---

# API Token Role in Permission Management

The `ApiTokensEndpoint` class manages API tokens. It uses `IsAuthenticated` to ensure that only authenticated users can interact with the endpoints. This class is crucial for managing permissions associated with API tokens.

```python
class ApiTokensEndpoint(Endpoint):
    owner = ApiOwner.SECURITY
    publish_status = {
        "DELETE": ApiPublishStatus.PRIVATE,
        "GET": ApiPublishStatus.PRIVATE,
        "POST": ApiPublishStatus.PRIVATE,
    }
    authentication_classes = (SessionNoAuthTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/api/endpoints/api_tokens.py" line="74">

---

# API Token Validation Process

The `post` method in `ApiTokensEndpoint` validates the API token. It checks if the provided data is valid and then creates a new token with specified scopes and types, ensuring that the token adheres to the defined permissions.

```python
        serializer = ApiTokenSerializer(data=request.data)

        if serializer.is_valid():
            result = serializer.validated_data

            token = ApiToken.objects.create(
                user_id=request.user.id,
                name=result.get("name", None),
                token_type=AuthTokenType.USER,
                scope_list=result["scopes"],
                expires_at=None,
            )

            capture_security_activity(
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

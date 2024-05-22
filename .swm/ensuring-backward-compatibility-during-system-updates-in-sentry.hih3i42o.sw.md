---
title: Ensuring Backward Compatibility During System Updates in Sentry
---
This document will explore how Sentry ensures backward compatibility during updates. We'll cover:

1. How legacy endpoints are maintained for backward compatibility.
2. Strategies for maintaining backward compatibility in serialization.

<SwmSnippet path="/src/sentry/api/endpoints/debug_files.py" line="381">

---

# Maintaining Legacy Endpoints

This section of the code demonstrates how Sentry maintains backward compatibility by keeping legacy endpoints. The `post` method in `AssociateDSymFilesEndpoint` is preserved to ensure that older integrations continue to function as expected even after updates.

```python
    # Legacy endpoint, kept for backwards compatibility
    def post(self, request: Request, project) -> Response:
        return Response({"associatedDsymFiles": []})
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/api/serializers/models/role.py" line="38">

---

# Serialization and Backward Compatibility

In the serialization process for roles, backward compatibility is ensured through conditional checks. For instance, the `is_retired_role` and `is_team_roles_allowed` fields are managed based on feature availability, which allows older role configurations to remain valid and functional.

```python
    def serialize(
        self,
        obj: Role,
        attrs: Mapping[str, Any],
        user: User,
        **kwargs: Any,
    ) -> BaseRoleSerializerResponse:
        has_team_roles = features.has("organizations:team-roles", self.organization)
        is_retired_role = has_team_roles and obj.is_retired

        allowed_roles = kwargs.get("allowed_roles") or ()

        return {
            "id": str(obj.id),
            "name": obj.name,
            "desc": obj.desc,
            "scopes": obj.scopes,
            "allowed": obj in allowed_roles,  # backward compatibility
            "isAllowed": obj in allowed_roles,
            "isRetired": is_retired_role,
            "isTeamRolesAllowed": obj.is_team_roles_allowed,
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

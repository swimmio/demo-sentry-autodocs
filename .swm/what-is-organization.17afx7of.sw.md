---
title: What is Organization
---
<SwmSnippet path="/src/sentry/services/hybrid_cloud/organization/service.py" line="472">

---

# Organization in Hybrid Cloud

In Sentry's hybrid cloud setup, the `Organization` concept is central to managing access and operations across different environments (e.g., regional, control, and monolith modes). The `OrganizationService` class handles the delegation of tasks based on the operational mode, ensuring that organization-related operations like checking and signaling are appropriately routed. This setup allows for flexible and efficient management of organization data and operations across various deployment scenarios.

```python
_organization_check_service: OrganizationCheckService = silo_mode_delegation(
    {
        SiloMode.REGION: _region_check_organization,
        SiloMode.CONTROL: _control_check_organization,
        SiloMode.MONOLITH: _region_check_organization,
    }
)


_organization_signal_service: OrganizationSignalService = silo_mode_delegation(
    {
        SiloMode.REGION: _signal_from_on_commit,
        SiloMode.CONTROL: _signal_from_outbox,
        SiloMode.MONOLITH: _signal_from_on_commit,
    }
)

organization_service = OrganizationService.create_delegation()
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/services/hybrid_cloud/organization/impl.py" line="69">

---

# Organization Membership Endpoints

The `check_membership_by_id` method is an endpoint that checks if a user is a member of a specific organization by their IDs. It attempts to find a member within the organization and returns a serialized member object if found, otherwise returns None.

```python
class DatabaseBackedOrganizationService(OrganizationService):
    def check_membership_by_id(
        self, organization_id: int, user_id: int
    ) -> RpcOrganizationMember | None:
        try:
            member = OrganizationMember.objects.get(
                user_id=user_id, organization_id=organization_id
            )
        except OrganizationMember.DoesNotExist:
            return None

        return serialize_member(member)
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/services/hybrid_cloud/organization/impl.py" line="96">

---

# Organization Retrieval Endpoints

The `get_organization_by_id` method serves as an endpoint to retrieve detailed context about an organization by its ID. It includes options to include projects and teams in the response, enhancing the detail of the organization context provided.

```python
    def get_organization_by_id(
        self,
        *,
        id: int,
        user_id: int | None = None,
        slug: str | None = None,
        include_projects: bool | None = True,
        include_teams: bool | None = True,
    ) -> RpcUserOrganizationContext | None:
        membership: RpcOrganizationMember | None = None
        if user_id is not None:
            membership = self.check_membership_by_id(organization_id=id, user_id=user_id)

        try:
            query = Organization.objects.filter(id=id)
            if slug is not None:
                query = query.filter(slug=slug)
            org = query.get()
        except Organization.DoesNotExist:
            return None

```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

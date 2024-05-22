---
title: Getting started with Project
---
# Project in Hybrid Cloud Service

In Sentry's hybrid cloud service, a 'Project' represents a logical entity within an organization, used to group and manage related error tracking and performance monitoring tasks. The `Project` is crucial for organizing the data collected from different applications or services. It is identified by attributes like ID, name, slug, and associated organization ID. Projects can be created, serialized, and managed through various functions such as `create_project_for_organization`, which sets up a new project within a specified organization, optionally linking it to the default team if specified. This function ensures that the project is correctly set up in the database and triggers events like `project_created` to handle any additional setup or notification required post-creation.

<SwmSnippet path="/src/sentry/services/hybrid_cloud/project/impl.py" line="24">

---

# Project Retrieval and Management Endpoints

The code defines multiple endpoints for managing projects within an organization. For instance, `get_by_id` retrieves a project by its ID, `get_many_by_organizations` fetches multiple projects within specified organizations, and `create_project_for_organization` and `get_or_create_project_for_organization` handle the creation of new projects. These functions utilize Django's ORM to interact with the database, ensuring that projects are fetched and managed efficiently.

```python
class DatabaseBackedProjectService(ProjectService):
    def get_by_id(self, *, organization_id: int, id: int) -> RpcProject | None:
        try:
            project = Project.objects.get_from_cache(id=id, organization=organization_id)
        except ValueError:
            project = Project.objects.filter(id=id, organization=organization_id).first()
        except Project.DoesNotExist:
            return None
        if project:
            return serialize_project(project)
        return None

    def get_many_by_organizations(
        self,
        *,
        region_name: str,
        organization_ids: list[int],
    ) -> list[RpcProject]:
        projects = Project.objects.filter(
            organization__in=organization_ids,
            status=ObjectStatus.ACTIVE,
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

---
title: VSTS 101
---
# VSTS Integration in Sentry

VSTS, now known as Azure DevOps, is integrated into Sentry to enhance error tracking and project management within development workflows. The integration allows Sentry to connect with Azure DevOps organizations, enabling features like automatic synchronization of commit data, linking Sentry issues to Azure DevOps work items, and managing deployments. This connection streamlines the process of tracking down and fixing bugs by linking code commits and deployment tracking directly to the errors captured by Sentry.

<SwmSnippet path="/src/sentry/integrations/vsts/repository.py" line="19">

---

# Repository Data Retrieval

This function `get_repository_data` is an endpoint that retrieves data about a specific repository from Azure DevOps using the VSTS API. It constructs the repository configuration by fetching details like project name, repository name, external ID, and URL.

```python
    def get_repository_data(
        self, organization: Organization, config: MutableMapping[str, Any]
    ) -> Mapping[str, str]:
        installation = self.get_installation(config.get("installation"), organization.id)
        instance = installation.instance
        client = installation.get_client(base_url=instance)

        repo_id = config["identifier"]

        try:
            repo = client.get_repo(repo_id)
        except Exception as e:
            raise installation.raise_error(e)
        config.update(
            {
                "instance": instance,
                "project": repo["project"]["name"],
                "name": repo["name"],
                "external_id": str(repo["id"]),
                "url": repo["_links"]["web"]["href"],
            }
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/vsts/webhooks.py" line="35">

---

# Work Item Webhook

The `WorkItemWebhook` class defines a POST endpoint for handling updates to work items in Azure DevOps. It processes webhook payloads, validates them, and updates the corresponding Sentry integration based on the changes in the work item.

```python
class WorkItemWebhook(Endpoint):
    owner = ApiOwner.INTEGRATIONS
    publish_status = {
        "POST": ApiPublishStatus.UNKNOWN,
    }
    authentication_classes = ()
    permission_classes = ()

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        try:
            data = request.data
            event_type = data["eventType"]
            external_id = get_vsts_external_id(data=request.data)
        except Exception as e:
            logger.info("vsts.invalid-webhook-payload", extra={"error": str(e)})
            return self.respond(status=status.HTTP_400_BAD_REQUEST)

        # https://docs.microsoft.com/en-us/azure/devops/service-hooks/events?view=azure-devops#workitem.updated
        if event_type == "workitem.updated":
            integration = integration_service.get_integration(
                provider=PROVIDER_KEY, external_id=external_id
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

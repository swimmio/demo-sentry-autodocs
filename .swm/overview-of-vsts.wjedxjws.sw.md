---
title: Overview of VSTS
---
# VSTS Integration in Sentry

VSTS, now known as Azure DevOps, is integrated into Sentry to enhance error tracking by connecting Sentry with Azure DevOps organizations. This integration allows users to streamline their workflow by linking Sentry issues directly to Azure DevOps work items, synchronizing comments and assignees, and augmenting Sentry issues with commit data from Azure DevOps repositories. This connection is facilitated through the `VstsIntegrationProvider` class, which handles the setup and configuration of the integration, including OAuth authentication and repository synchronization.

<SwmSnippet path="/src/sentry/integrations/vsts/repository.py" line="19">

---

# Repository Data Endpoint

This segment of code defines an endpoint for fetching repository data from Azure DevOps. It utilizes the `get_repo` method from the client to retrieve repository details using the repository ID (`repo_id`). The retrieved data is then used to update the configuration with details such as instance, project name, repository name, external ID, and URL.

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

# Work Item Webhook Endpoint

This endpoint handles POST requests for work item updates in Azure DevOps. It checks the validity of the webhook payload, identifies the integration using the external ID, and processes the updated work item data accordingly. The endpoint specifically handles the 'workitem.updated' event type, ensuring that updates are synchronized with Sentry's integration data.

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

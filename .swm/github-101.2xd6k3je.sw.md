---
title: GitHub 101
---
<SwmSnippet path="/src/sentry/integrations/github/integration.py" line="292">

---

# GitHub Integration in Sentry

GitHub is a platform for version control and collaboration, allowing users to manage and store revisions of projects. In the context of Sentry, specifically within the `src/sentry/integrations/github` directory, GitHub is integrated to enhance error tracking by linking Sentry issues with GitHub commits, issues, and pull requests. This integration facilitates better tracking and resolution of errors by connecting code changes directly to the Sentry platform, allowing for a seamless workflow between code management and error monitoring.

```python
class GitHubIntegrationProvider(IntegrationProvider):
    key = "github"
    name = "GitHub"
    metadata = metadata
    integration_cls = GitHubIntegration
    features = frozenset(
        [
            IntegrationFeatures.COMMITS,
            IntegrationFeatures.ISSUE_BASIC,
            IntegrationFeatures.STACKTRACE_LINK,
            IntegrationFeatures.CODEOWNERS,
        ]
    )

    setup_dialog_config = {"width": 1030, "height": 1000}

    def get_client(self) -> GitHubClientMixin:
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/github/repository.py" line="35">

---

# GitHub Repository Endpoints

This section of the code uses the GitHub API to check repository hooks, specifically using the endpoint defined in the GitHub documentation for listing repository hooks. This is crucial for validating that the Sentry installation has the necessary permissions to access the repository.

```python
            # https://docs.github.com/en/rest/webhooks/repo-config#list-hooks
            client.repo_hooks(repo)
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/github/search.py" line="24">

---

# GitHub Search Endpoint

This code defines a search endpoint for GitHub and GitHub Enterprise integrations within Sentry. It handles GET requests to search for issues or repositories based on user queries, utilizing GitHub's search API endpoints. The response handling includes error checks for rate limits and access issues, which are common with GitHub's API.

```python
    def get(
        self, request: Request, organization: RpcOrganization, integration_id: int, **kwds: Any
    ) -> Response:
        try:
            integration = Integration.objects.get(
                organizationintegration__organization_id=organization.id,
                id=integration_id,
            )
        except Integration.DoesNotExist:
            return Response(status=404)

        field = request.GET.get("field")
        query = request.GET.get("query")
        if field is None:
            return Response({"detail": "field is a required parameter"}, status=400)
        if not query:
            return Response({"detail": "query is a required parameter"}, status=400)

        installation = integration.get_installation(organization.id)
        if field == "externalIssue":
            repo = request.GET.get("repo")
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

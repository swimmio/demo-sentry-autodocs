---
title: Introduction to GitHub
---
<SwmSnippet path="/src/sentry/integrations/github/integration.py" line="292">

---

# GitHub Integration in Sentry

GitHub is a platform for version control and collaboration, allowing users to manage and store revisions of projects. In the context of Sentry, GitHub is integrated to enhance error tracking by linking Sentry issues with GitHub commits, issues, and pull requests. This integration facilitates better tracking and resolution of errors by providing direct links to the source code and related GitHub activities. The `GitHubIntegrationProvider` class in Sentry configures this integration, setting up features like commit tracking and issue linking, which are crucial for maintaining efficient workflows between code management and error resolution.

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

<SwmSnippet path="/src/sentry/integrations/github/repository.py" line="23">

---

# GitHub Repository Endpoints

This section of the code defines methods related to GitHub repository management. The `_validate_repo` method specifically interacts with GitHub's repository and hooks endpoints to ensure Sentry has the necessary access to the repository. It uses GitHub's API to fetch repository data and validate permissions.

```python
    def _validate_repo(
        self, client: Any, installation: IntegrationInstallation, repo: str
    ) -> JSONData:
        try:
            repo_data = client.get_repo(repo)
        except Exception as e:
            raise installation.raise_error(e)

        try:
            # make sure installation has access to this specific repo
            # use hooks endpoint since we explicitly ask for those permissions
            # when installing the app (commits can be accessed for public repos)
            # https://docs.github.com/en/rest/webhooks/repo-config#list-hooks
            client.repo_hooks(repo)
        except ApiError:
            raise IntegrationError(f"You must grant Sentry access to {repo}")

        return repo_data
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/github/search.py" line="16">

---

# GitHub Search Endpoint

This file defines a search endpoint for GitHub and GitHub Enterprise integrations. It handles GET requests to search for issues or repositories based on user queries. The method `get` uses the GitHub API to perform searches and handle potential errors like rate limits.

```python
@control_silo_endpoint
class GithubSharedSearchEndpoint(IntegrationEndpoint):
    owner = ApiOwner.ECOSYSTEM
    publish_status = {
        "GET": ApiPublishStatus.PRIVATE,
    }
    """NOTE: This endpoint is a shared search endpoint for Github and Github Enterprise integrations."""

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
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

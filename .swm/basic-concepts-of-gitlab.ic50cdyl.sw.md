---
title: Basic concepts of GitLab
---
# GitLab Integration in Sentry

GitLab is a web-based DevOps lifecycle tool that provides a Git repository manager providing wiki, issue-tracking, and CI/CD pipeline features. In the Sentry context, specifically within the `src/sentry/integrations/gitlab` directory, GitLab is integrated to enhance error tracking by linking code in a GitLab repository with issues occurring in Sentry. Features enabled by this integration include tracking commits and releases, resolving issues via GitLab commits and merge requests, and creating GitLab issues directly from Sentry incidents. This integration facilitates a more streamlined workflow between code changes and error monitoring, allowing developers to address and resolve errors more efficiently.

<SwmSnippet path="/src/sentry/integrations/gitlab/webhooks.py" line="241">

---

# GitLab Webhook Endpoints

The `GitlabWebhookEndpoint` class defines the endpoint for handling incoming GitLab webhooks. It processes POST requests, extracts the necessary GitLab event data, and dispatches it to the appropriate handler based on the event type, such as 'Push Hook' or 'Merge Request Hook'. This setup is crucial for integrating GitLab's event system with Sentry's error tracking and performance monitoring capabilities.

```python
class GitlabWebhookEndpoint(Endpoint, GitlabWebhookMixin):
    owner = ApiOwner.INTEGRATIONS
    publish_status = {
        "POST": ApiPublishStatus.PRIVATE,
    }
    authentication_classes = ()
    permission_classes = ()
    provider = "gitlab"

    _handlers = handlers

    @method_decorator(csrf_exempt)
    def dispatch(self, request: Request, *args, **kwargs) -> HttpResponse:
        if request.method != "POST":
            return HttpResponse(status=405, reason="HTTP method not supported.")

        return super().dispatch(request, *args, **kwargs)

    def post(self, request: Request) -> HttpResponse:
        clear_tags_and_context()
        extra = {
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/gitlab/webhooks.py" line="88">

---

# Handling Merge Request and Push Events

This section of the code handles specific GitLab webhook events. The `MergeEventWebhook` and `PushEventWebhook` classes are designed to process merge request events and push events, respectively. They update repository data and handle specific attributes of the events such as commits and merge requests, integrating these into Sentry's system for tracking and analysis.

```python
class MergeEventWebhook(Webhook):
    """
    Handle Merge Request Hook

    See https://docs.gitlab.com/ee/user/project/integrations/webhooks.html#merge-request-events
    """

    def __call__(
        self, integration: RpcIntegration, organization: Organization, event: Mapping[str, Any]
    ):
        repo = self.get_repo(integration, organization, event)
        if repo is None:
            return

        # while we're here, make sure repo data is up to date
        self.update_repo_data(repo, event)

        try:
            number = event["object_attributes"]["iid"]
            title = event["object_attributes"]["title"]
            body = event["object_attributes"]["description"]
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

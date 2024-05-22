---
title: Basic concepts of Bitbucket
---
# Bitbucket Integration in Sentry

Bitbucket is a web-based version control repository hosting service owned by Atlassian, used for source code and development projects that use either Mercurial or Git revision control systems. In the context of Sentry, Bitbucket integration allows users to connect their Sentry organization with their Bitbucket repositories. This integration facilitates several features such as tracking commits and releases, resolving issues via Bitbucket commits, and creating Bitbucket issues directly from Sentry. This enhances the workflow between code management and error tracking, making it more efficient for developers to manage and rectify errors in their applications.

<SwmSnippet path="/src/sentry/integrations/bitbucket/installed.py" line="13">

---

# Bitbucket Installed Endpoint

This endpoint handles the POST request for the Bitbucket integration when it is installed. It uses the `BitbucketIntegrationProvider` to build the integration data from the request state and ensures the integration with Bitbucket is established.

```python
@control_silo_endpoint
class BitbucketInstalledEndpoint(Endpoint):
    owner = ApiOwner.INTEGRATIONS
    publish_status = {
        "POST": ApiPublishStatus.UNKNOWN,
    }
    authentication_classes = ()
    permission_classes = ()

    @csrf_exempt
    def dispatch(self, request: Request, *args, **kwargs) -> Response:
        return super().dispatch(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs) -> Response:
        state = request.data
        data = BitbucketIntegrationProvider().build_integration(state)
        ensure_integration("bitbucket", data)

        return self.respond()
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/bitbucket/search.py" line="17">

---

# Bitbucket Search Endpoint

This endpoint facilitates the search functionality within the Bitbucket integration. It supports searching for issues and repositories based on provided query parameters. The response includes formatted data suitable for Sentry's use, handling both successful searches and errors like missing issue trackers.

```python
@control_silo_endpoint
class BitbucketSearchEndpoint(IntegrationEndpoint):
    owner = ApiOwner.INTEGRATIONS
    publish_status = {
        "GET": ApiPublishStatus.UNKNOWN,
    }

    def get(self, request: Request, organization, integration_id, **kwds) -> Response:
        try:
            integration = Integration.objects.get(
                organizationintegration__organization_id=organization.id,
                id=integration_id,
                provider="bitbucket",
            )
        except Integration.DoesNotExist:
            return Response(status=404)

        field = request.GET.get("field")
        query = request.GET.get("query")
        if field is None:
            return Response({"detail": "field is a required parameter"}, status=400)
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

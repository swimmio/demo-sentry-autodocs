---
title: Integration of CI/CD Pipelines in Sentrys Release Utilities
---
This document will explore how Sentry integrates CI/CD pipelines within its Release Utilities, focusing on:

<SwmSnippet path="/src/sentry/integrations/pipeline.py" line="83">

---

# Integration Pipeline

The `IntegrationPipeline` class is a crucial component in Sentry's integration process with CI/CD pipelines. It manages the integration lifecycle, including authentication, data handling, and error management. This class uses the `finish_pipeline` method to finalize the integration process, handling data received from the CI/CD pipeline and ensuring that the integration is correctly set up in Sentry's system.

```python
class IntegrationPipeline(Pipeline):
    pipeline_name = "integration_pipeline"
    provider_manager = default_manager

    def get_analytics_entry(self) -> PipelineAnalyticsEntry | None:
        pipeline_type = "reauth" if self.fetch_state("integration_id") else "install"
        return PipelineAnalyticsEntry("integrations.pipeline_step", pipeline_type)

    def finish_pipeline(self):
        try:
            data = self.provider.build_integration(self.state.data)
        except IntegrationError as e:
            self.get_logger().info(
                "build-integration.failure",
                extra={
                    "error_message": str(e),
                    "error_status": getattr(e, "code", None),
                    "provider_key": self.provider.key,
                },
            )
            return self.error(str(e))
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/web/frontend/integration_extension_configuration.py" line="19">

---

# External Integration Pipeline

The `ExternalIntegrationPipeline` class extends `IntegrationPipeline` to handle specific cases where integrations need to redirect to external configuration pages. This is particularly useful for integrating third-party services that require additional configuration steps that are not handled within Sentry's standard pipeline flow.

```python
class ExternalIntegrationPipeline(IntegrationPipeline):
    def _dialog_success(self, _org_integration):
        org_slug = self.organization.slug
        provider = self.provider.integration_key
        integration_id = self.integration.id
        # add in param string if we have a next page
        param_string = ""
        if "next" in self.request.GET:
            param_string = "?%s" % urlencode({"next": self.request.GET["next"]})

        redirect_uri = self.organization.absolute_url(
            f"/settings/{org_slug}/integrations/{provider}/{integration_id}/",
            query=param_string,
        )
        return HttpResponseRedirect(redirect_uri)
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

---
title: Configuring CI/CD Pipelines in Sentry
---
This document will explore how CI/CD pipelines are configured in Sentry, focusing on:

# Overview of CI/CD Pipelines in Sentry

Sentry's CI/CD pipelines are designed to execute a series of views that maintain arbitrary state across each request, guiding the user through the pipeline process. This involves executing set views that receive the pipeline instance and move through them by having the view itself call `pipeline.next_step`. State can be maintained within the pipeline using the `pipeline.bind_state` method.

<SwmSnippet path="/src/sentry/integrations/pipeline.py" line="83">

---

# IntegrationPipeline Class

The `IntegrationPipeline` class extends the `Pipeline` class and is specifically tailored for handling integrations. It manages the pipeline's state and data throughout the integration process, including error handling and logging. The `finish_pipeline` method finalizes the integration process, handling data building and error management.

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

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

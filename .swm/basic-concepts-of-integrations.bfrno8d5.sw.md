---
title: Basic concepts of Integrations
---
# Integrations in Sentry

In Sentry, 'Integrations' refer to the connections established between Sentry and external services or platforms, enhancing its functionality. These integrations can range from version control systems like GitHub, communication platforms like Discord, to cloud services like AWS Lambda. Each integration typically involves authentication processes, data synchronization, and specific features like issue tracking, commit tracking, or alert notifications. For example, GitHub integration allows tracking commits, pull requests, and other GitHub events directly within Sentry. Similarly, Discord integration might handle user authentication and link Sentry issues with Discord identities.

<SwmSnippet path="/src/sentry/integrations/aws_lambda/integration.py" line="75">

---

# AWS Lambda Integration Endpoints

This section of the code defines several endpoints for managing AWS Lambda functions through Sentry's integration. It includes methods to enable, disable, and update Lambda functions to the latest version, leveraging Sentry's error tracking and performance monitoring capabilities.

```python
class AwsLambdaIntegration(IntegrationInstallation, ServerlessMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._client = None

    @property
    def region(self):
        return self.metadata["region"]

    @property
    def client(self):
        if not self._client:
            region = self.metadata["region"]
            account_number = self.metadata["account_number"]
            aws_external_id = self.metadata["aws_external_id"]
            self._client = gen_aws_client(
                account_number=account_number,
                region=region,
                aws_external_id=aws_external_id,
            )

```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

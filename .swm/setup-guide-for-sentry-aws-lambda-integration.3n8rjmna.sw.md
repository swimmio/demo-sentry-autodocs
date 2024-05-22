---
title: Setup Guide for Sentry AWS Lambda Integration
---
This document will guide you through the steps required to integrate Sentry with an AWS Lambda project, covering the following aspects:

1. Preparing your AWS environment
2. Configuring Sentry in your AWS Lambda functions

# Preparing your AWS Environment

Before integrating Sentry, ensure that your AWS account has the necessary permissions to create and modify AWS Lambda functions. This includes IAM roles and policies that allow for the creation of Lambda functions and the attachment of additional resources like layers and environment variables.

<SwmSnippet path="/src/sentry/integrations/aws_lambda/utils.py" line="206">

---

# Configuring Sentry in your AWS Lambda Functions

This function `enable_single_lambda` is crucial for integrating Sentry into an AWS Lambda function. It handles the addition of the Sentry layer to your Lambda, sets the necessary environment variables, and updates the function's configuration to use Sentry for error tracking and performance monitoring.

```python
def enable_single_lambda(lambda_client, function, sentry_project_dsn, retries_left=3):
    # find the latest layer for this function
    layer_arn = get_latest_layer_for_function(function)

    name = function["FunctionName"]
    runtime = function["Runtime"]
    # update the env variables
    env_variables = function.get("Environment", {}).get("Variables", {})

    # Check if the sentry sdk layer already exists
    layers = get_function_layer_arns(function)
    sentry_layer_index = get_index_of_sentry_layer(layers, layer_arn)

    updated_handler = None

    sentry_env_variables = {
        "SENTRY_DSN": sentry_project_dsn,
        "SENTRY_TRACES_SAMPLE_RATE": "1.0",
    }

    if runtime.startswith("nodejs"):
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

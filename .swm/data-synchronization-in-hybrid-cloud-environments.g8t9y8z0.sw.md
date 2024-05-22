---
title: Data Synchronization in Hybrid Cloud Environments
---
This document will explore the mechanisms of data synchronization between cloud and on-premises environments in Sentry's hybrid cloud setup. We'll cover:

1. How data synchronization is structured within Sentry's codebase.
2. Key components involved in the synchronization process.

# Data Synchronization Structure

The `integration_service` module plays a crucial role in managing data synchronization tasks between cloud and on-premises environments. It handles the logic for syncing data across different environments, ensuring consistency and reliability.

<SwmSnippet path="/src/sentry/tasks/integrations/sync_status_outbound.py" line="3">

---

# Key Components in Synchronization

This script is part of the outbound data synchronization process. It utilizes the `integration_service` to update external systems with the latest status from Sentry's internal state, ensuring that data remains synchronized across different platforms.

```python
from sentry.models.integrations.external_issue import ExternalIssue
from sentry.models.integrations.integration import Integration
from sentry.services.hybrid_cloud.integration import integration_service
from sentry.silo.base import SiloMode
from sentry.tasks.base import instrumented_task, retry, track_group_async_operation
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

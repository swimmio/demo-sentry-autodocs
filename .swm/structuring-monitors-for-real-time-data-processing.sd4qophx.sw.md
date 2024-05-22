---
title: Structuring Monitors for Real-Time Data Processing
---
This document will explore the structure and functionality of the real-time data processing in Sentry's Monitors sub-component. Key areas covered include:

1. Overview of the real-time metrics processing architecture
2. Detailed examination of Redis implementation for real-time metrics

<SwmSnippet path="/src/sentry/processing/realtime_metrics/base.py" line="1">

---

# Real-Time Metrics Processing Architecture

This section of the code defines the base architecture for real-time metrics processing. It includes abstract classes and base methods that outline the necessary components and their interactions for processing real-time data.

```python
from collections.abc import Iterable

from sentry.utils.services import Service


class RealtimeMetricsStore(Service):
    """A service for storing metrics about incoming requests within a given time window."""

    __all__ = (
        "validate",
        "record_project_duration",
        "projects",
        "get_used_budget_for_project",
        "get_lpq_projects",
        "is_lpq_project",
        "add_project_to_lpq",
        "remove_projects_from_lpq",
    )

    def validate(self) -> None:
        """
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/processing/realtime_metrics/redis.py" line="1">

---

# Redis Implementation for Real-Time Metrics

This file implements the Redis backend for real-time metrics processing. It details how data is structured, stored, and accessed in Redis to facilitate efficient real-time data processing.

```python
import logging
from collections.abc import Iterable, Sequence
from time import time

from sentry.exceptions import InvalidConfiguration
from sentry.utils import redis

from . import base

# redis key for entry storing current list of LPQ members
LPQ_MEMBERS_KEY = "store.symbolicate-event-lpq-selected"

logger = logging.getLogger(__name__)


class RedisRealtimeMetricsStore(base.RealtimeMetricsStore):
    """An implementation of RealtimeMetricsStore based on a Redis backend."""

    def __init__(
        self,
        cluster: str,
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

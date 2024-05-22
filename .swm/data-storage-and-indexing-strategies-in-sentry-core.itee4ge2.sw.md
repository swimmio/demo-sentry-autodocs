---
title: Data Storage and Indexing Strategies in Sentry Core
---
This document will explore how data storage and indexing are managed in Sentry to facilitate quick data retrieval. We'll cover:

1. How data is structured for efficient access.
2. The role of indexing in enhancing data retrieval speeds.

<SwmSnippet path="/src/sentry/sentry_metrics/consumers/indexer/processing.py" line="31">

---

# Data Structuring for Efficient Access

The `STORAGE_TO_INDEXER` mapping in Sentry defines how different storage backends are associated with specific indexer implementations. This setup allows for flexible and optimized data storage strategies, which are crucial for efficient data retrieval.

```python
STORAGE_TO_INDEXER: Mapping[IndexerStorage, Callable[[], StringIndexer]] = {
    IndexerStorage.POSTGRES: PostgresIndexer,
    IndexerStorage.MOCK: MockIndexer,
}
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/sentry_metrics/consumers/indexer/processing.py" line="42">

---

# Indexing to Enhance Data Retrieval

Here, the indexer is initialized based on the configured database backend. This indexer plays a critical role in managing how data is indexed, which directly impacts the retrieval speeds by allowing quick lookups and efficient data access patterns.

```python
    def __init__(self, config: MetricsIngestConfiguration):
        self._indexer = STORAGE_TO_INDEXER[config.db_backend](**config.db_backend_options)
        self._config = config
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

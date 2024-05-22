---
title: Data Security and Privacy in AWS Lambda Sentry Integration
---
This document will cover the mechanisms Sentry employs to ensure that sensitive data is not inadvertently sent to its servers. We'll explore:

1. How Sentry filters sensitive data.
2. Code configurations that help prevent sensitive data leakage.

<SwmSnippet path="/src/sentry/utils/safe.py" line="11">

---

# How Sentry Filters Sensitive Data

Sentry utilizes the `sentry.utils.json` module, which is designed to safely handle data serialization and ensure that sensitive information is not leaked in the process.

```python
from sentry.db.postgres.transactions import django_test_transaction_water_mark
from sentry.utils import json
from sentry.utils.strings import truncatechars
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

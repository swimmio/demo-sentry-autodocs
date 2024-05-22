---
title: >-
  Methods for Handling Data Schema Changes in Sentrys Data Transformation
  Component
---
This document will explore the methods Sentry uses to handle data schema changes, focusing on:

<SwmSnippet path="/src/sentry/db/postgres/schema.py" line="12">

---

# Handling Data Schema Changes

This section of the code defines various unsafe operations related to schema changes, such as adding columns with defaults or altering column types. Each operation is associated with a warning and a link to further documentation on how to perform these operations safely.

```python
unsafe_mapping = {
    Unsafe.ADD_COLUMN_DEFAULT: (
        "Adding {}.{} as column with a default is safe, but you need to take additional steps.\n"
        "Follow this guide: https://develop.sentry.dev/database-migrations/#adding-columns-with-a-default"
    ),
    Unsafe.ADD_COLUMN_NOT_NULL: (
        "Adding {}.{} as a not null column is unsafe.\n"
        "More info: https://develop.sentry.dev/database-migrations/#adding-not-null-to-columns"
    ),
    Unsafe.ALTER_COLUMN_TYPE: (
        "Altering the type of column {}.{} in this way is unsafe\n"
        "More info here: https://develop.sentry.dev/database-migrations/#altering-column-types"
    ),
    # TODO: If we use > 3.0 we can add tests to verify this
    Unsafe.ADD_CONSTRAINT_EXCLUDE: (
        "Adding an exclusion constraint is unsafe\n"
        "We don't use these at Sentry currently, bring this up in #discuss-backend"
    ),
    Unsafe.ALTER_TABLE_SET_TABLESPACE: (
        "Changing the tablespace for a table is unsafe\n"
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/db/postgres/schema.py" line="101">

---

# Schema Validation and Editing

The `DatabaseSchemaEditorProxy` class provides a mechanism to switch between safe and unsafe schema editing modes. This flexibility is crucial for managing schema changes safely, especially in a production environment.

```python
class DatabaseSchemaEditorProxy:
    """
    Wrapper that allows us to use either the `SafePostgresDatabaseSchemaEditor` or
    `PostgresDatabaseSchemaEditor`. Can be configured by setting the `safe` property
    before using to edit the schema. If already in use, attempts to modify `safe` will
    fail.
    """

    class AlreadyInUse(Exception):
        pass

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self._safe = False
        self._schema_editor = None

    @property
    def safe(self):
        return self._safe

```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

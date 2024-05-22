---
title: Handling Schema Migrations in Production for Sentry
---
This document will cover the handling of schema migrations in a production environment for Sentry, focusing on:

<SwmSnippet path="/src/sentry/migrations/0707_alert_rule_activations_incidents_fk.py" line="10">

---

# Schema Migration Strategy

This section of the code defines a class `Migration` which includes a flag `is_post_deployment`. This flag indicates whether the migration should be run automatically in production or not. It's set to `False` here, suggesting that this particular migration should be run as part of the deployment process.

```python
class Migration(CheckedMigration):
    # This flag is used to mark that a migration shouldn't be automatically run in production.
    # This should only be used for operations where it's safe to run the migration after your
    # code has deployed. So this should not be used for most operations that alter the schema
    # of a table.
    # Here are some things that make sense to mark as post deployment:
    # - Large data migrations. Typically we want these to be run manually so that they can be
    #   monitored and not block the deploy for a long period of time while they run.
    # - Adding indexes to large tables. Since this can take a long time, we'd generally prefer to
    #   run this outside deployments so that we don't block them. Note that while adding an index
    #   is a schema change, it's completely safe to run the operation after the code has deployed.
    # Once deployed, run these manually via: https://develop.sentry.dev/database-migrations/#migration-deployment

```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/new_migrations/migrations.py" line="19">

---

# Applying Migrations

The `apply` method in the `Migration` class is crucial for applying migrations in the production environment. It checks if the migration has been marked as safe and then proceeds with applying it using the `schema_editor`. This method ensures that migrations are applied safely and correctly in the production database.

```python
    def apply(self, project_state, schema_editor, collect_sql=False):
        if self.checked:
            schema_editor.safe = True
        return super().apply(project_state, schema_editor, collect_sql)
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

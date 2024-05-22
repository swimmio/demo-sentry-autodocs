---
title: Data Integrity and Migration Management in Sentry
---
This document will explore how Sentry manages data integrity and handles migrations within its ecosystem. Key areas covered include:

1. The role of migrations in Sentry's data management.
2. Customizations and safety measures in migration processes.
3. Examples of migration scripts and their purposes.

<SwmSnippet path="/src/sentry/runner/commands/migrations.py" line="11">

---

# Sentry's Migration Management

This code snippet from `migrations.py` shows the initialization of migration processes in Sentry. It includes custom patches through `monkeypatch_django_migrations` and environment settings to manage dangerous migrations.

```python
def migrations() -> None:
    from sentry.runner.initializer import monkeypatch_django_migrations

    # Include our monkeypatches for migrations.
    monkeypatch_django_migrations()

    # Allow dangerous/postdeploy migrations to be run.
    os.environ["MIGRATION_SKIP_DANGEROUS"] = "0"
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/runner/initializer.py" line="473">

---

# Custom Migration Handling

Here, Sentry customizes Django's migration executor to ensure data integrity during migrations. The `monkey_migrations` function from `sentry.new_migrations.monkey` is applied to enhance the migration process.

```python
def monkeypatch_django_migrations() -> None:
    # This monkeypatches django's migration executor with our own, which
    # adds some small but important customizations.
    from sentry.new_migrations.monkey import monkey_migrations

    monkey_migrations()
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

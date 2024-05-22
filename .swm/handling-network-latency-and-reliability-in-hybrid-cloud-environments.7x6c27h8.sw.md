---
title: Handling Network Latency and Reliability in Hybrid Cloud Environments
---
This document will explore how Sentry handles network latency and reliability in hybrid cloud environments, focusing on:

<SwmSnippet path="/src/sentry/tasks/deletion/hybrid_cloud.py" line="180">

---

# Network Latency and Reliability Handling

The function `_process_hybrid_cloud_foreign_key_cascade` is crucial for managing data consistency across distributed environments, which is a key aspect of handling network latency and reliability in hybrid cloud setups. It ensures that foreign key constraints are respected even when deletions occur, which could be across different network zones, thus maintaining data integrity and system reliability.

```python
def _process_hybrid_cloud_foreign_key_cascade(
    app_name: str, model_name: str, field_name: str, process_task: Task, silo_mode: SiloMode
) -> None:
    """
    Called by the silo bound tasks above.
    """
    try:
        model = apps.get_model(app_label=app_name, model_name=model_name)
        try:
            field = model._meta.get_field(field_name)
            if not isinstance(field, HybridCloudForeignKey):
                raise Exception(f"The {field_name} field is not a HybridCloudForeignKey")
        except Exception as err:
            sentry_sdk.capture_exception(err)
            raise LookupError(f"Could not find field {field_name} on model {app_name}.{model_name}")

        tombstone_cls = TombstoneBase.class_for_silo_mode(silo_mode)
        assert tombstone_cls, "A tombstone class is required"

        # We rely on the return value of _process_tombstone_reconciliation
        # to short circuit the second half of this `or` so that the terminal batch
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

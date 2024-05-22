---
title: Efficient Change Propagation in Sentrys Options System
---
This document will explore how changes are efficiently propagated in the Options system without impacting performance. We'll cover:

1. The role of the `_update_project_configs` function in managing changes.
2. How the `schedule_invalidate_project_config` function ensures efficient change propagation.

<SwmSnippet path="/src/sentry/killswitches.py" line="27">

---

# Managing Changes in the Options System

The `_update_project_configs` function is crucial for managing changes in the Options system. It checks for changes in project configurations and schedules updates only for the changed projects, ensuring minimal performance impact.

```python
def _update_project_configs(
    old_option_value: Sequence[Mapping[str, Any]], new_option_value: Sequence[Mapping[str, Any]]
) -> None:
    """Callback for the relay.drop-transaction-metrics kill switch.
    On every change, force a recomputation of the corresponding project configs
    """
    from sentry.models.organization import Organization
    from sentry.tasks.relay import schedule_invalidate_project_config

    old_project_ids = {ctx["project_id"] for ctx in old_option_value}
    new_project_ids = {ctx["project_id"] for ctx in new_option_value}

    # We want to recompute the project config for any project that was added
    # or removed
    changed_project_ids = old_project_ids ^ new_project_ids

    if None in changed_project_ids:
        with click.progressbar(length=Organization.objects.count()) as bar:  # type: ignore[var-annotated]  # pallets/click#2630
            # Since all other invalidations, which would happen anyway, will de-duplicate
            # with these ones the extra load of this is reasonable.  A temporary backlog in
            # the relay_config_bulk queue is just fine.  We have server-side cursors
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

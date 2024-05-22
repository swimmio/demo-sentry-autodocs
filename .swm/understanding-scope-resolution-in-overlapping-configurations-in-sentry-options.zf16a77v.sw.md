---
title: Understanding Scope Resolution in Overlapping Configurations in Sentry Options
---
This document will explore how scope resolution is managed in scenarios with overlapping configurations in Sentry's codebase. Key points include:

1. How scope and object parameters determine processing issues resolution.
2. The role of type specificity in resolving processing issues.

<SwmSnippet path="/src/sentry/models/processingissue.py" line="31">

---

# Scope and Object Parameters

The function `resolve_processing_issue` uses `scope` and `object` parameters to determine which processing issues to resolve. It filters issues based on these parameters and optionally by `type` if it is specified, showcasing how Sentry handles scope resolution in overlapping configurations.

```python
    def resolve_processing_issue(self, project, scope, object, type=None):
        """Resolves the given processing issues.  If not type is given
        all processing issues for scope and object are resolved regardless
        of the type.
        """
        checksum = get_processing_issue_checksum(scope, object)
        q = ProcessingIssue.objects.filter(project=project, checksum=checksum)
        if type is not None:
            q = q.filter(type=type)
        q.delete()
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/models/processingissue.py" line="38">

---

# Type Specificity in Resolution

This segment of the `resolve_processing_issue` function demonstrates how specifying a `type` can further refine the resolution process. If `type` is provided, the query filters processing issues not just by `scope` and `object`, but also by the specific `type`, allowing for precise control over which issues are resolved in cases of overlapping configurations.

```python
        if type is not None:
            q = q.filter(type=type)
        q.delete()
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

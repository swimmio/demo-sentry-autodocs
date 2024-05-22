---
title: Understanding Sentrys Build Automation Process
---
This document will explain the automation of the build process in Sentry, focusing on key aspects:

1. How assets are determined to need building
2. The steps involved in building assets
3. Integration of documentation building in the build process.

<SwmSnippet path="/src/sentry/utils/distutils/commands/build_assets.py" line="95">

---

# Determining the Need for Building Assets

The `_needs_built` function checks if the assets need to be built by verifying the current package version and comparing it with the static version information.

```python
    def _needs_built(self):
        if BaseBuildCommand._needs_built(self):
            return True
        version_info = self._get_package_version()
        return self._needs_static(version_info)
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

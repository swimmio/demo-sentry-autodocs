---
title: Tools Used in Sentrys Build Automation
---
This document will explore the tools used in Sentry's build automation process, focusing on:

# Build Automation Tools in Sentry

Sentry utilizes a variety of tools to manage and automate the build process. These tools are primarily located in the `tools` directory and include scripts for linting, dependency management, and other utilities essential for maintaining code quality and consistency.

<SwmSnippet path="/tools/lint_requirements.py" line="1">

---

# Build Automation Tools in Sentry

This script, `lint_requirements.py`, is part of Sentry's build automation tools. It ensures that Python package requirements are correctly formatted and adhere to defined specifications.

```python
from __future__ import annotations

import argparse
from collections.abc import Sequence

import packaging.requirements


def main(argv: Sequence[str] | None = None) -> int:
    """
    We cannot have non-specifier requirements if we want to publish to PyPI
    due to security concerns. This check ensures we don't have/add any URL/VCS
    dependencies in the base requirements file.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    for filename in args.filenames:
        with open(filename) as reqs_file:
            for lineno, line in enumerate(reqs_file, start=1):
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

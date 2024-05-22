---
title: Handling Polymorphism in Sentry Models
---
This document will explore how polymorphism is handled in the models within Sentry's codebase, specifically focusing on the implementation of polymorphic rules in dynamic sampling.

# Overview of Polymorphism in Models

Polymorphism in programming allows objects of different classes to be treated as objects of a common superclass. It is a core concept in object-oriented programming that enables a single interface to represent different underlying forms (data types).

<SwmSnippet path="/src/sentry/dynamic_sampling/rules/logging.py" line="5">

---

# Implementation of Polymorphic Rules

The `PolymorphicRule` class is imported and utilized within the dynamic sampling rules module. This class likely serves as a base or interface for various types of sampling rules, demonstrating polymorphism by allowing different rule types to be treated uniformly.

```python
from sentry.dynamic_sampling.rules.utils import (
    DecayingFn,
    PolymorphicRule,
    RuleType,
    get_rule_hash,
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

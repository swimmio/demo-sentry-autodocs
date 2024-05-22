---
title: Getting started
---
This document will guide you through the initial steps to get started with Sentry, covering key aspects such as:

# Sentry Overview

Sentry is a developer-first error tracking and performance monitoring platform that helps developers see what actually matters, solve quicker, and learn continuously about their applications. It supports multiple programming languages and platforms.

# Important Documents

Before diving into Sentry, it's recommended to read the `README.md` for a general overview, and the `CONTRIBUTING.md` to understand how to contribute to the repository.

<SwmSnippet path="/webpack.config.ts" line="241">

---

# Running and Debugging

The main webpack configuration for Sentry's React SPA is defined here. It includes settings for development and production environments, handling of various file types, and optimizations.

```typescript
const appConfig: Configuration = {
  mode: WEBPACK_MODE,
  entry: {
    /**
     * Main Sentry SPA
     *
     * The order here matters for `getsentry`
     */
    app: ['sentry/utils/statics-setup', 'sentry'],

    /**
     * Pipeline View for integrations
     */
    pipeline: ['sentry/utils/statics-setup', 'sentry/views/integrationPipeline'],

    /**
     * Legacy CSS Webpack appConfig for Django-powered views.
     * This generates a single "sentry.css" file that imports ALL component styles
     * for use on Django-powered pages.
     */
    sentry: 'less/sentry.less',
```

---

</SwmSnippet>

# How to Contribute

To contribute to Sentry, you can start by looking at the `Contributing to Sentry` section in the `CONTRIBUTING.md` file, which guides you through the setup, and how to make pull requests.

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

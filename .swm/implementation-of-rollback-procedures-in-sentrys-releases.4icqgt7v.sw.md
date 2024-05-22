---
title: Implementation of Rollback Procedures in Sentrys Releases
---
This document will explore the rollback procedures for releases in Sentry, focusing on:

# Rollback Procedures for Releases

Rollback procedures in Sentry are crucial for reverting a release to a previous state if the current release introduces bugs or breaks functionality. The process involves identifying the release to be rolled back, determining the last stable state, and executing the rollback to restore the system to that state.

<SwmSnippet path="/static/app/views/dashboards/datasetConfig/releases.tsx" line="385">

---

# Implementation of Rollback Procedures

The `getReleasesRequest` function is a central part of managing releases, including potential rollbacks. It fetches release data based on specific conditions, which can be adjusted to handle different scenarios, including rollbacks.

```tsx
function getReleasesRequest(
  includeSeries: number,
  includeTotals: number,
  api: Client,
  query: WidgetQuery,
  organization: Organization,
  pageFilters: PageFilters,
  interval?: string,
  limit?: number,
  cursor?: string
) {
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

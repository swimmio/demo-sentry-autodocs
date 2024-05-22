---
title: Scaling Techniques in Monitors
---
This document will explore the techniques used in Sentry's Monitors to ensure effective scaling. We'll cover:

1. How Monitors manage data queries and rendering
2. The use of hooks for fetching and managing Monitor stats

<SwmSnippet path="/static/app/views/monitors/components/monitorStats.tsx" line="31">

---

# Data Management in Monitors

This section of the code demonstrates how Monitors handle data queries efficiently. The `MonitorStats` component uses a time range to fetch data, which is determined by either the user's selection or a default range. This approach ensures that only the necessary data is loaded, enhancing performance as the application scales.

```tsx
function MonitorStats({monitor, monitorEnvs, orgSlug}: Props) {
  const {selection} = usePageFilters();
  const {start, end, period} = selection.datetime;

  const nowRef = useRef(new Date());

  let since: number, until: number;
  if (start && end) {
    until = new Date(end).getTime() / 1000;
    since = new Date(start).getTime() / 1000;
  } else {
    until = Math.floor(nowRef.current.getTime() / 1000);
    const intervalSeconds = intervalToMilliseconds(period ?? '30d') / 1000;
    since = until - intervalSeconds;
  }

  const queryKey = [
```

---

</SwmSnippet>

<SwmSnippet path="/static/app/views/monitors/components/timeline/hooks/useMonitorStats.tsx" line="21">

---

# Fetching and Managing Monitor Stats

Here, the `useMonitorStats` hook is used to fetch and manage Monitor stats. It takes a list of monitor IDs and a time window configuration, making API calls to fetch stats. The use of hooks and the structuring of API calls based on the component's needs help in managing state and side effects efficiently, contributing to the scalability of Monitors.

```tsx
export function useMonitorStats({monitors, timeWindowConfig}: Options) {
  const {start, end, elapsedMinutes, timelineWidth} = timeWindowConfig;

  const rollup = Math.floor((elapsedMinutes * 60) / timelineWidth);

  const selectionQuery = {
    since: Math.floor(start.getTime() / 1000),
    until: Math.floor(end.getTime() / 1000),
    resolution: `${rollup}s`,
  };

  const organization = useOrganization();
  const router = useRouter();
  const location = router.location;

  const monitorStatsQueryKey = `/organizations/${organization.slug}/monitors-stats/`;

  return useApiQuery<Record<string, MonitorBucketData>>(
    [
      monitorStatsQueryKey,
      {
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

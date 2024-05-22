---
title: Extensibility Features for Sentry Dashboards
---
This document will explore the extensibility features available in Sentry for third-party integrations or custom widget development. Key areas covered include:

1. How visualization components are structured for extensibility.
2. The role of the `Widget` type in enabling custom widget configurations.
3. The process of updating widgets through API endpoints.

<SwmSnippet path="/static/app/views/performance/landing/widgets/widgets/vitalWidget.tsx" line="321">

---

# Visualization Components

The `visualizations` constant demonstrates how Sentry allows for conditional rendering of components based on feature availability, which is a core aspect of its extensibility for third-party integrations. This setup enables the injection of custom components or modifications based on specific conditions.

```tsx
  const visualizations = organization.features.includes('performance-new-widget-designs')
    ? [
        {
          component: provided => (
            <Accordion
              expandedIndex={selectedListIndex}
              setExpandedIndex={setSelectListIndex}
              items={assembleAccordionItems(provided)}
            />
          ),
          // accordion items height + chart height
          height: TOTAL_EXPANDABLE_ROWS_HEIGHT + props.chartHeight,
          noPadding: true,
        },
```

---

</SwmSnippet>

<SwmSnippet path="/static/app/views/dashboards/metrics/utils.tsx" line="15">

---

# Widget Type and Configuration

The `Widget` type definition in Sentry's codebase is crucial for understanding how widgets can be configured and extended. This type includes various properties that dictate how widgets behave and are displayed, which is essential for developing custom widgets or integrating third-party services.

```tsx
  type DashboardFilters,
  DisplayType,
  type Widget,
  type WidgetQuery,
  WidgetType,
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

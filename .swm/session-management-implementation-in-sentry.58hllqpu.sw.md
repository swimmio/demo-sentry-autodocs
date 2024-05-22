---
title: Session Management Implementation in Sentry
---
This document will explore the mechanisms of session management within Sentry, focusing on how sessions are defined, manipulated, and utilized across different components of the application. Key areas covered include:

1. Definition and structure of session data types.
2. Operations and calculations performed on session data.
3. Integration of session management in UI components and API requests.

<SwmSnippet path="/static/app/types/sessions.tsx" line="7">

---

# Session Data Types and Structures

The `SessionsMeta` type and `SessionField` enum define the structure and possible fields of session data in Sentry. These definitions are crucial for understanding how session data is structured and manipulated within the application.

```tsx
export type SessionsMeta = {
  name: string;
  operations: SessionsOperation[];
  type: ColumnType;
};

export enum SessionField {
  SESSION = 'session',
  SESSION_DURATION = 'session.duration',
  USER = 'user',
}

export type SessionsOperation =
  | 'sum'
  | 'count_unique'
  | 'crash_rate'
  | 'crash_free_rate'
  | 'count_abnormal'
  | 'count_errored'
  | 'count_healthy'
  | 'count_crashed'
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

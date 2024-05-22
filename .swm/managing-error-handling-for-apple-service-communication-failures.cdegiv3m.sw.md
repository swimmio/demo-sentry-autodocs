---
title: Managing Error Handling for Apple Service Communication Failures
---
This document will cover the error handling mechanisms used when there is a failure in communication with Apple's services in Sentry's codebase. We'll explore:

1. How errors are structured and handled in general
2. Specific error handling for communication failures with Apple's services

<SwmSnippet path="/static/app/views/settings/components/dataScrubbing/modals/handleError.tsx" line="20">

---

# General Error Handling Structure

This code snippet from `handleError` function demonstrates how Sentry structures and handles errors internally. It checks for various error messages and categorizes them into types such as `UNKNOWN`, `INVALID_SELECTOR`, and `REGEX_PARSE`. This structure is crucial for understanding how specific errors, like those from Apple's services, would be handled.

```tsx
function handleError(error: ResponseError): Error {
  const errorMessage = error.responseJSON?.relayPiiConfig[0];

  if (!errorMessage) {
    return {
      type: ErrorType.UNKNOWN,
      message: t('Unknown error occurred while saving data scrubbing rule'),
    };
  }

  if (errorMessage.startsWith('invalid selector: ')) {
    for (const line of errorMessage.split('\n')) {
      if (line.startsWith('1 | ')) {
        const selector = line.slice(3);
        return {
          type: ErrorType.INVALID_SELECTOR,
          message: t('Invalid source value: %s', selector),
        };
      }
    }
  }
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

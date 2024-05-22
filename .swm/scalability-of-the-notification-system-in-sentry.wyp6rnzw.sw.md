---
title: Scalability of the Notification System in Sentry
---
This document will explore how Sentry's notification system is designed to scale effectively. We'll cover:

1. The structure and components of the notification system.
2. How new notification types and services are added to the system.

# Notification System Structure

Sentry's notification system is built to be highly scalable and configurable. It uses a model called `NotificationAction`, which is an abstraction from `AlertRuleTriggerAction`. This model allows notifications to be sent to third-party integrations and can be configured across an entire organization or project, rather than per recipient. This design supports scalability by decoupling the notification actions from specific issues, events, or incidents, and instead focusing on the integration level.

# Adding New Notification Types and Services

To add new types of triggers, services, or targets to the notification system, developers can extend the relevant enums in `notificationaction.py`. This flexibility allows Sentry to easily scale by integrating new services and notification types as needed without major overhauls to the existing system.

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

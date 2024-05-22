---
title: Managing Notification Preferences in Sentry
---
This document will explore how notification preferences are managed and stored in Sentry, focusing on:

# Overview of Notification Preferences

Notification preferences in Sentry are managed through a combination of user settings and system configurations that determine how notifications are sent and received. These settings can be adjusted per user or across projects and organizations.

<SwmSnippet path="/src/sentry/api/endpoints/user_notification_settings_options.py" line="28">

---

# Managing Notification Preferences

This code snippet from `user_notification_settings_options.py` shows how the notification preferences for a user are retrieved and managed. It filters notification settings based on the user ID and the type of notification, allowing for customization of notification preferences.

```python
    def get(self, request: Request, user: User) -> Response:
        """
        Retrieve the notification preferences for a user.
        Returns a list of NotificationSettingOption rows.
        """
        notification_type = request.GET.get("type")
        notifications_settings = NotificationSettingOption.objects.filter(user_id=user.id)
        if notification_type:
            try:
                validate_type(notification_type)
            except ParameterValidationError:
                return self.respond({"type": ["Invalid type"]}, status=status.HTTP_400_BAD_REQUEST)
            notifications_settings = notifications_settings.filter(type=notification_type)

        notification_preferences = serialize(
            list(notifications_settings), request.user, NotificationSettingsOptionSerializer()
        )

        return Response(notification_preferences)
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

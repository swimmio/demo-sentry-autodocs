---
title: Handling and Customization of Email Templates
---
This document will explore the mechanisms Sentry uses for handling and customizing email templates based on error types or user preferences. We'll cover:

1. How email templates are structured and customized.
2. The process of handling email templates in response to different error types and user preferences.

<SwmSnippet path="/src/sentry/templates/sentry/partial/interfaces/user_email.html" line="1">

---

# Email Template Structure and Customization

This HTML template file is used to define the structure of email content based on user data. It includes conditional rendering of user information such as ID, IP address, username, and email, which can be customized per the requirements of different error notifications or user preferences.

```html
{% load i18n %}
{% load sentry_avatars %}
{% load sentry_helpers %}
<table class="reset">
  <tr>
    <td>
      <table>
        <colgroup>
          <col style="width:130px;">
        </colgroup>
        <tbody>
          {% if user_id %}
            <tr>
              <th>{% trans "ID:" %}</th>
              <td class="code">{{ user_id }}</td>
            </tr>
            {% endif %}
          {% if user_ip_address %}
            <tr>
              <th>{% trans "IP Address:" %}</th>
              <td class="code">{{ user_ip_address }}</td>
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/utils/email/message_builder.py" line="79">

---

# Handling Email Templates

The `__init__` method in `MessageBuilder` class is crucial for setting up email messages. It allows customization of the email subject, body, and headers based on the type of error or user preference. This method also handles the inclusion of dynamic data through the `context` parameter, which can be tailored to include specific error details or user information.

```python
    def __init__(
        self,
        subject: str,
        context: Mapping[str, Any] | None = None,
        template: str | None = None,
        html_template: str | None = None,
        body: str = "",
        html_body: str | None = None,
        headers: Mapping[str, str] | None = None,
        reference: Model | None = None,
        from_email: str | None = None,
        type: str | None = None,
    ) -> None:
        assert not (body and template)
        assert not (html_body and html_template)
        assert context or not (template or html_template)

        self.subject = subject
        self.context = context or {}
        self.template = template
        self.html_template = html_template
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

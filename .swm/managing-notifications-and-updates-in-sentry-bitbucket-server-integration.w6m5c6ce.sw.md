---
title: Managing Notifications and Updates in Sentry-Bitbucket Server Integration
---
This document will explore how notifications and updates are managed between Sentry and Bitbucket Server, focusing on:

<SwmSnippet path="/src/sentry/integrations/bitbucket_server/integration.py" line="1">

---

# Integration Setup

This file contains the setup for the Bitbucket Server integration in Sentry. It includes the initialization of the integration, configuration settings, and the connection between Sentry and Bitbucket Server.

```python
from __future__ import annotations

import logging
from typing import Any
from urllib.parse import urlparse

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from django import forms
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from rest_framework.request import Request

from sentry.integrations import (
    FeatureDescription,
    IntegrationFeatures,
    IntegrationInstallation,
    IntegrationMetadata,
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/bitbucket_server/webhook.py" line="1">

---

# Notification Handling

This file manages webhook events from Bitbucket Server. It processes incoming HTTP requests that contain updates or notifications related to the repositories monitored by Sentry.

```python
import logging
from datetime import datetime, timezone

import sentry_sdk
from django.db import IntegrityError, router, transaction
from django.http import HttpResponse
from django.http.response import HttpResponseBase
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from rest_framework.request import Request

from sentry.models.commit import Commit
from sentry.models.commitauthor import CommitAuthor
from sentry.models.integrations.integration import Integration
from sentry.models.organization import Organization
from sentry.models.repository import Repository
from sentry.plugins.providers import IntegrationRepositoryProvider
from sentry.shared_integrations.exceptions import ApiHostError, ApiUnauthorized, IntegrationError
from sentry.utils import json
from sentry.web.frontend.base import region_silo_view
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

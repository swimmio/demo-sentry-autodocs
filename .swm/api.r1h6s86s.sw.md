---
title: API
---
This document will cover the Sentry API, focusing on its offerings and how developers can interact with it:

<SwmSnippet path="/api-docs/openapi.json" line="1">

---

# Sentry API Overview

The Sentry API is defined in the `openapi.json` file, which outlines various endpoints for teams, organizations, projects, events, and more. It serves as the central definition for the API's capabilities.

```json
{
  "openapi": "3.0.1",
  "info": {
    "title": "API Reference",
    "description": "Sentry Public API",
    "termsOfService": "http://sentry.io/terms/",
    "contact": {
      "email": "partners@sentry.io"
    },
    "license": {
      "name": "Apache 2.0",
      "url": "http://www.apache.org/licenses/LICENSE-2.0.html"
    },
    "version": "v0"
  },
  "servers": [
    {
      "url": "https://sentry.io/"
    }
  ],
  "tags": [
```

---

</SwmSnippet>

<SwmSnippet path="/api-docs/openapi.json" line="89">

---

# Finding API Endpoints

The list of API endpoints can be found in the `openapi.json` file under the `paths` section. This includes detailed references for each endpoint, such as operations on teams, projects, and organizations.

```json
  "paths": {
    "/api/0/teams/{organization_slug}/{team_id_or_slug}/": {
      "$ref": "paths/teams/by-slug.json"
    },
    "/api/0/teams/{organization_slug}/{team_id_or_slug}/stats/": {
      "$ref": "paths/teams/stats.json"
    },
    "/api/0/organizations/": {
      "$ref": "paths/organizations/index.json"
    },
    "/api/0/organizations/{organization_slug}/eventids/{event_id}/": {
      "$ref": "paths/organizations/event-id-lookup.json"
    },
    "/api/0/organizations/{organization_slug}/": {
      "$ref": "paths/organizations/details.json"
    },
    "/api/0/organizations/{organization_slug}/repos/": {
      "$ref": "paths/organizations/repos.json"
    },
    "/api/0/organizations/{organization_slug}/repos/{repo_id}/commits/": {
      "$ref": "paths/organizations/repo-commits.json"
```

---

</SwmSnippet>

# Swagger

The API is available via Swagger. The specification path is defined in the `openapi.json` file, which includes all the necessary details for interacting with the API using Swagger tools.

# Postman

Currently, there is no direct citation for Postman collections in the provided context. However, typically, the API available via Swagger can also be imported into Postman for easier testing and interaction.

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

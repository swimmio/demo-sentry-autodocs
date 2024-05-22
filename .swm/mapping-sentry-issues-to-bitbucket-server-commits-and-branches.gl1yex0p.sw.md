---
title: Mapping Sentry Issues to Bitbucket Server Commits and Branches
---
This document will cover the process Sentry uses to map issues to specific commits or branches in Bitbucket Server, including:

1. How Sentry retrieves commit information from Bitbucket Server.
2. How Sentry maps these commits to issues.

<SwmSnippet path="/src/sentry/integrations/bitbucket_server/client.py" line="26">

---

# Retrieving Commit Information

Sentry uses the `commit_changes` endpoint to retrieve commit information from Bitbucket Server. This endpoint is defined in the `BitbucketServerAPIPath` class and is used to fetch changes associated with a specific commit.

```python
    repository_commits = "/rest/api/1.0/projects/{project}/repos/{repo}/commits"
    repository_commit_details = "/rest/api/1.0/projects/{project}/repos/{repo}/commits/{commit}"
    commit_changes = "/rest/api/1.0/projects/{project}/repos/{repo}/commits/{commit}/changes"
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/bitbucket_server/repository.py" line="134">

---

# Mapping Commits to Issues

The `_transform_patchset` function in `BitbucketServerRepositoryProvider` processes the commit data fetched from Bitbucket Server. It transforms the patch data into Sentry's internal format, which is then used to map commits to issues based on file changes and commit messages.

```python
    def _transform_patchset(self, values):
        """Convert the patch data from Bitbucket into our internal format

        See sentry.models.Release.set_commits
        """
        changes = []
        for change in values:
            if change["type"] == "MODIFY":
                changes.append({"path": change["path"]["toString"], "type": "M"})
            if change["type"] == "ADD":
                changes.append({"path": change["path"]["toString"], "type": "A"})
            if change["type"] == "DELETE":
                changes.append({"path": change["path"]["toString"], "type": "D"})
            if change["type"] == "MOVE":
                changes.append({"path": change["srcPath"]["toString"], "type": "D"})
                changes.append({"path": change["path"]["toString"], "type": "A"})
        return changes
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

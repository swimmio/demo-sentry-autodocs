---
title: Flow of Comparing Commits in Bitbucket Server Integration
---
This document outlines the flow of comparing commits in the Bitbucket Server integration within Sentry. The flow involves several steps, each contributing to the process of comparing commits for a repository:

```mermaid
graph TD;
  compare_commits::src/sentry/integrations/bitbucket_server/repository.py:::mainFlowStyle --> _format_commits::src/sentry/integrations/bitbucket_server/repository.py
  compare_commits::src/sentry/integrations/bitbucket_server/repository.py:::mainFlowStyle --> bcw2i[...]
  _format_commits::src/sentry/integrations/bitbucket_server/repository.py:::mainFlowStyle --> _get_patchset::src/sentry/integrations/bitbucket_server/repository.py
  _get_patchset::src/sentry/integrations/bitbucket_server/repository.py:::mainFlowStyle --> get_commit_filechanges::src/sentry/integrations/bitbucket_server/client.py
  _get_patchset::src/sentry/integrations/bitbucket_server/repository.py:::mainFlowStyle --> ai9yr[...]
  get_commit_filechanges::src/sentry/integrations/bitbucket_server/client.py:::mainFlowStyle --> _get_values::src/sentry/integrations/bitbucket_server/client.py
  get_commit_filechanges::src/sentry/integrations/bitbucket_server/client.py:::mainFlowStyle --> gvy9u[...]
  _get_values::src/sentry/integrations/bitbucket_server/client.py:::mainFlowStyle --> copy::src/sentry/sdk_updates.py
  copy::src/sentry/sdk_updates.py:::mainFlowStyle --> ...

 classDef mainFlowStyle color:#000000,fill:#7CB9F4
```

<SwmSnippet path="/src/sentry/integrations/bitbucket_server/repository.py" line="87">

---

# Initiate Commit Comparison

The `compare_commits` function initiates the process of comparing commits. It formats each commit in the list using the `_format_commits` function, which structures commit data and prepares it for further processing.

```python
    def _format_commits(self, client, repo, commit_list):
        return [
            {
                "id": c["id"],
                "repository": repo.name,
                "author_email": c["author"]["emailAddress"],
                "author_name": c["author"].get("displayName", c["author"]["name"]),
                "message": c["message"],
                "timestamp": datetime.fromtimestamp(c["authorTimestamp"] / 1000, timezone.utc),
                "patch_set": self._get_patchset(
                    client, repo.config["project"], repo.config["repo"], c["id"]
                ),
            }
            for c in commit_list
        ]
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/bitbucket_server/repository.py" line="87">

---

# Format Commits

The `_format_commits` function takes a list of commits and formats them. Each commit is processed to extract and format relevant data such as the commit ID, author, message, and timestamp. It also initiates fetching the patch set for each commit by calling `_get_patchset`.

```python
    def _format_commits(self, client, repo, commit_list):
        return [
            {
                "id": c["id"],
                "repository": repo.name,
                "author_email": c["author"]["emailAddress"],
                "author_name": c["author"].get("displayName", c["author"]["name"]),
                "message": c["message"],
                "timestamp": datetime.fromtimestamp(c["authorTimestamp"] / 1000, timezone.utc),
                "patch_set": self._get_patchset(
                    client, repo.config["project"], repo.config["repo"], c["id"]
                ),
            }
            for c in commit_list
        ]
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/bitbucket_server/repository.py" line="121">

---

# Fetch Patch Set

The `_get_patchset` function is responsible for fetching the patch set of a commit, which includes the changes made in that commit. It calls `get_commit_filechanges` to retrieve the file changes from the Bitbucket Server.

```python
    def _get_patchset(self, client, project, repo, sha):
        """
        Get the modified files for a commit
        """

        key = f"get_changelist:{md5_text(project + repo).hexdigest()}:{sha}"
        commit_files = cache.get(key)
        if commit_files is None:
            commit_files = client.get_commit_filechanges(project, repo, sha)
            cache.set(key, commit_files, 900)

        return self._transform_patchset(commit_files)
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/bitbucket_server/client.py" line="196">

---

# Retrieve Commit File Changes

The `get_commit_filechanges` function fetches the file changes for a specific commit from the Bitbucket Server. It constructs the API path and queries the server, handling pagination through `_get_values`.

```python
    def get_commit_filechanges(self, project, repo, commit, limit=1000):
        logger.info(
            "load.filechanges",
            extra={
                "bitbucket_repo": repo,
                "bitbucket_project": project,
                "bitbucket_commit": commit,
            },
        )

        return self._get_values(
            BitbucketServerAPIPath.commit_changes.format(project=project, repo=repo, commit=commit),
            {"limit": limit},
        )
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/integrations/bitbucket_server/client.py" line="211">

---

# Handle Paginated API Responses

The `_get_values` function handles the pagination of API responses. It iteratively requests pages of data until all values are retrieved or the last page is reached, ensuring complete data retrieval for processing.

```python
    def _get_values(self, uri, params, max_pages=1000000):
        values = []
        start = 0

        logger.info(
            "load.paginated_uri",
            extra={
                "bitbucket_uri": uri,
                "bitbucket_max_pages": max_pages,
                "bitbucket_params": params,
            },
        )

        for i in range(max_pages):
            new_params = dict.copy(params)
            new_params["start"] = start
            logger.debug(
                "Loading values for paginated uri starting from %s",
                start,
                extra={"uri": uri, "params": new_params},
            )
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

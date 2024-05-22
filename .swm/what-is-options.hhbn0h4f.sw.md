---
title: What is Options
---
# Overview of Options

In Sentry, `Options` refer to configurations that can be set at different levels such as system-wide, organization, project, or user level. These configurations control various aspects of Sentry's behavior and features. For instance, `Option` and `ControlOption` classes in `src/sentry/models/options/option.py` define the base structure for options, which include key-value pairs stored in the database. The `OptionMixin` class provides methods like `get_option`, `update_option`, and `delete_option` to interact with these options. These methods are utilized across different models like `Organization`, `Project`, and `User` to fetch or modify settings specific to that context, affecting how features like error tracking and notifications behave.

<SwmSnippet path="/src/sentry/models/options/user_option.py" line="27">

---

# UserOptionManager Methods

The `UserOptionManager` class provides several methods to manipulate user options. Methods like `get_value`, `set_value`, `unset_value`, and `get_all_values` allow for setting, getting, and deleting user options. These options can be scoped to different levels (user, project, organization) based on the parameters provided.

```python
class UserOptionManager(OptionManager["UserOption"]):
    def _make_key(  # type: ignore[override]
        self,
        user: User | RpcUser | int,
        project: Project | int | None = None,
        organization: Organization | int | None = None,
    ) -> str:
        uid = user.id if user and not isinstance(user, int) else user
        org_id: int | None = organization.id if isinstance(organization, Model) else organization
        proj_id: int | None = project.id if isinstance(project, Model) else project
        if project:
            metakey = f"{uid}:{proj_id}:project"
        elif organization:
            metakey = f"{uid}:{org_id}:organization"
        else:
            metakey = f"{uid}:user"

        return super()._make_key(metakey)

    def get_value(
        self, user: User | RpcUser, key: str, default: Value | None = None, **kwargs: Any
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/models/options/user_option.py" line="146">

---

# UserOption Model

The `UserOption` model defines the structure for user options in Sentry. It includes fields like `user`, `project_id`, `organization_id`, `key`, and `value`. This model supports flexible foreign keys to link with user, project, and organization, and uses a `PickledObjectField` for the value to accommodate various data types.

```python
class UserOption(Model):
    """
    User options apply only to a user, and optionally a project OR an organization.

    Options which are specific to a plugin should namespace
    their key. e.g. key='myplugin:optname'

    Keeping user feature state
    key: "feature:assignment"
    value: { updated: datetime, state: bool }

    where key is one of:
     (please add to this list if adding new keys)
     - clock_24_hours
        - 12hr vs. 24hr
     - issue:defaults
        - only used in Jira, set default reporter field
     - issues:defaults:jira
        - unused
     - issues:defaults:jira_server
        - unused
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

---
title: Structure of User Permissions Model in Sentry
---
This document will explore the structure of the user permissions model in Sentry, focusing on how permissions are managed and assigned to users. Key areas covered include:

1. How permissions are added to a user
2. How permissions are listed for a user

<SwmSnippet path="/src/sentry/runner/commands/permissions.py" line="33">

---

# How Permissions are Added to a User

This section of the code defines the `add` command which is used to add permissions to a user. It utilizes the `UserPermission` model to create a new permission entry in the database. If the permission already exists, it catches an `IntegrityError` and notifies the user.

```python
@permissions.command()
@click.option("--user", "-u", default=None, required=True)
@click.option("--permission", "-p", default=None, required=True)
@configuration
def add(user: str, permission: str) -> None:
    "Add a permission to a user."
    from django.db import IntegrityError, transaction

    from sentry.models.userpermission import UserPermission

    user_inst = user_param_to_user(user)

    try:
        with transaction.atomic(router.db_for_write(UserPermission)):
            UserPermission.objects.create(user=user_inst, permission=permission)
    except IntegrityError:
        click.echo(f"Permission already exists for `{user_inst.username}`")
    else:
        click.echo(f"Added permission `{permission}` to `{user_inst.username}`")
```

---

</SwmSnippet>

<SwmSnippet path="/src/sentry/runner/commands/permissions.py" line="76">

---

# How Permissions are Listed for a User

This part of the code handles the `list` command, which lists all permissions assigned to a specific user. It retrieves permissions from the `UserPermission` model and displays them. This function is crucial for auditing and managing user permissions effectively.

```python
def list(user: str) -> None:
    "List permissions for a user."
    from sentry.models.userpermission import UserPermission

    user_inst = user_param_to_user(user)
    up_list = UserPermission.objects.filter(user=user_inst).order_by("permission")
    click.echo(f"Permissions for `{user_inst.username}`:")
    for permission in up_list:
        click.echo(f"- {permission.permission}")
```

---

</SwmSnippet>

&nbsp;

*This is an auto-generated document by Swimm AI 🌊 and has not yet been verified by a human*

<SwmMeta version="3.0.0" repo-id="Z2l0aHViJTNBJTNBc2VudHJ5JTNBJTNBZ2V0c2VudHJ5" repo-name="sentry"><sup>Powered by [Swimm](/)</sup></SwmMeta>

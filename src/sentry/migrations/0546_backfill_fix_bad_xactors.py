# Generated by Django 3.2.20 on 2023-08-01 20:51

from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps

from sentry.new_migrations.migrations import CheckedMigration
from sentry.utils.query import RangeQuerySetWrapperWithProgressBar


def backfill_xactor(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    ExternalActor = apps.get_model("sentry", "ExternalActor")

    for xa in RangeQuerySetWrapperWithProgressBar(
        ExternalActor.objects.filter(team_id__isnull=True, user_id__isnull=True)
    ):
        actor = xa.actor
        if actor.team_id is None and actor.user_id is None:
            # Defunct
            xa.delete()
            continue

        xa.user_id = actor.user_id
        xa.team_id = actor.team_id
        xa.save()


class Migration(CheckedMigration):
    # This flag is used to mark that a migration shouldn't be automatically run in production. For
    # the most part, this should only be used for operations where it's safe to run the migration
    # after your code has deployed. So this should not be used for most operations that alter the
    # schema of a table.
    # Here are some things that make sense to mark as post deployment:
    # - Large data migrations. Typically we want these to be run manually by ops so that they can
    #   be monitored and not block the deploy for a long period of time while they run.
    # - Adding indexes to large tables. Since this can take a long time, we'd generally prefer to
    #   have ops run this and not block the deploy. Note that while adding an index is a schema
    #   change, it's completely safe to run the operation after the code has deployed.
    is_post_deployment = False

    dependencies = [
        ("sentry", "0545_add_last_verified_auth_ident_replica"),
    ]

    operations = [
        migrations.RunPython(
            backfill_xactor,
            migrations.RunPython.noop,
            hints={"tables": ["sentry_externalactor", "sentry_actor"]},
        ),
    ]

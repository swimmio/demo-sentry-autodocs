# Generated by Django 2.2.28 on 2023-05-19 17:25

from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps

from sentry.new_migrations.migrations import CheckedMigration
from sentry.utils.query import RangeQuerySetWrapperWithProgressBar


def _backfill(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    cls = apps.get_model("sentry", "ProjectOption")

    for obj in RangeQuerySetWrapperWithProgressBar(cls.objects.all()):
        # load pickle, save json
        obj.save(update_fields=["value"])


class Migration(CheckedMigration):
    # data migration: must be run out of band
    is_post_deployment = True

    # data migration: run outside of a transaction
    atomic = False

    dependencies = [
        ("sentry", "0676_apitoken_hashed_indexes"),
    ]

    operations = [
        migrations.RunPython(
            _backfill,
            migrations.RunPython.noop,
            hints={"tables": ["sentry_projectoptions"]},
        ),
    ]
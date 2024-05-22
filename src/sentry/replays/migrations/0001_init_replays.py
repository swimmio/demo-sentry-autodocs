# Generated by Django 2.2.28 on 2022-07-21 22:16

import django.utils.timezone
from django.db import migrations, models

import sentry.db.models.fields.bounded
from sentry.new_migrations.migrations import CheckedMigration


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

    # This flag is used to decide whether to run this migration in a transaction or not. Generally
    # we don't want to run in a transaction here, since for long running operations like data
    # back-fills this results in us locking an increasing number of rows until we finally commit.
    atomic = False

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ReplayRecordingSegment",
            fields=[
                (
                    "id",
                    sentry.db.models.fields.bounded.BoundedBigAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                ("project_id", sentry.db.models.fields.bounded.BoundedBigIntegerField()),
                ("replay_id", models.CharField(db_index=True, max_length=32)),
                ("file_id", sentry.db.models.fields.bounded.BoundedBigIntegerField(db_index=True)),
                ("sequence_id", sentry.db.models.fields.bounded.BoundedIntegerField()),
                (
                    "date_added",
                    models.DateTimeField(db_index=True, default=django.utils.timezone.now),
                ),
            ],
            options={
                "db_table": "replays_replayrecordingsegment",
                "unique_together": {
                    ("project_id", "replay_id", "sequence_id"),
                    ("project_id", "replay_id", "file_id"),
                },
                "index_together": {("replay_id", "sequence_id")},
            },
        ),
    ]
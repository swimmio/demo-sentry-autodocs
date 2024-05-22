# Generated by Django 3.2.20 on 2023-08-30 18:32

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import sentry.db.models.fields.bounded
import sentry.db.models.fields.foreignkey
import sentry.db.models.fields.hybrid_cloud_foreign_key
import sentry.db.models.fields.jsonfield
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

    dependencies = [
        ("sentry", "0540_add_release_threshold_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuthProviderReplica",
            fields=[
                (
                    "id",
                    sentry.db.models.fields.bounded.BoundedBigAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "auth_provider_id",
                    sentry.db.models.fields.hybrid_cloud_foreign_key.HybridCloudForeignKey(
                        "sentry.AuthProvider", db_index=True, unique=True, on_delete="CASCADE"
                    ),
                ),
                ("provider", models.CharField(max_length=128)),
                ("config", sentry.db.models.fields.jsonfield.JSONField(default=dict)),
                (
                    "default_role",
                    sentry.db.models.fields.bounded.BoundedPositiveIntegerField(default=50),
                ),
                ("default_global_access", models.BooleanField(default=True)),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "organization",
                    sentry.db.models.fields.foreignkey.FlexibleForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sentry.organization",
                        unique=True,
                    ),
                ),
                ("allow_unlinked", models.BooleanField()),
                ("scim_enabled", models.BooleanField()),
            ],
            options={
                "db_table": "sentry_authproviderreplica",
            },
        ),
        migrations.CreateModel(
            name="AuthIdentityReplica",
            fields=[
                (
                    "id",
                    sentry.db.models.fields.bounded.BoundedBigAutoField(
                        primary_key=True, serialize=False
                    ),
                ),
                (
                    "auth_identity_id",
                    sentry.db.models.fields.hybrid_cloud_foreign_key.HybridCloudForeignKey(
                        "sentry.AuthIdentity", db_index=True, unique=True, on_delete="CASCADE"
                    ),
                ),
                (
                    "user_id",
                    sentry.db.models.fields.hybrid_cloud_foreign_key.HybridCloudForeignKey(
                        "sentry.User", db_index=True, on_delete="CASCADE"
                    ),
                ),
                (
                    "auth_provider_id",
                    sentry.db.models.fields.hybrid_cloud_foreign_key.HybridCloudForeignKey(
                        "sentry.AuthProvider", db_index=True, on_delete="CASCADE"
                    ),
                ),
                ("ident", models.CharField(max_length=128)),
                ("data", sentry.db.models.fields.jsonfield.JSONField(default=dict)),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                "db_table": "sentry_authidentityreplica",
                "unique_together": {("auth_provider_id", "user_id"), ("auth_provider_id", "ident")},
            },
        ),
    ]
from sentry.backup.scopes import RelocationScope
from sentry.db.models import BoundedBigIntegerField, Model, region_silo_only_model, sane_repr


@region_silo_only_model
class LatestRepoReleaseEnvironment(Model):
    """
    For each environment, tracks the latest release which is associated with
    commits in the given repo.
    """

    __relocation_scope__ = RelocationScope.Excluded

    repository_id = BoundedBigIntegerField()
    # 0 for 'all environments'
    environment_id = BoundedBigIntegerField()
    release_id = BoundedBigIntegerField()
    # deploy_id and commit_id are nullable but in practice always have a value
    deploy_id = BoundedBigIntegerField(null=True)
    # commit_id is the id of the ReleaseHeadCommit associated with the given release
    commit_id = BoundedBigIntegerField(null=True)

    class Meta:
        app_label = "sentry"
        db_table = "sentry_latestrelease"
        unique_together = (("repository_id", "environment_id"),)

    __repr__ = sane_repr("repository_id", "environment_id", "release_id")

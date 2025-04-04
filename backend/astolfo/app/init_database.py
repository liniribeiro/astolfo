from fastapi.logger import logger

from backend.astolfo.app.database.migrations import upgrade
from backend.astolfo.app.database.migrations.config import alembic_cfg
from backend.astolfo.app.database.models.base import DeclarativeBase
from backend.astolfo.app.database.session import sync_session, sync_engine
from backend.astolfo.app.settings import settings
from alembic import command

def upgrade_or_create():
    """
    Apply any missing migrations to an already init'd databsae. If it's
    a new database, fully create and skip migrations.
    """
    with sync_session() as session:
        table_exists = session.scalar(
            "SELECT count(*) FROM information_schema.tables"
            " WHERE table_name = 'listicle' and table_catalog = :db_name",
            {"db_name": settings.POSTGRES_DB},
        )

    if table_exists:
        upgrade()
    else:
        try:
            # Fresh database, create everything
            print("New database: create_all started")
            DeclarativeBase.metadata.create_all(bind=sync_engine)
            print("New database: create_all finished")
        except Exception as e:
            logger.error(e)
            raise e

        # Stamp as having all migrations applied
        command.stamp(alembic_cfg, "head")


if __name__ == "__main__":
    upgrade_or_create()
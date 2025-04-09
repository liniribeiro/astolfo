from fastapi.logger import logger
from sqlalchemy_utils import database_exists

from database.migrations import upgrade
from database.migrations.config import alembic_cfg
from database.models.base import DeclarativeBase
from database.session import sync_engine
from settings import settings
from alembic import command

def upgrade_or_create():
    """
    Apply any missing migrations to an already init'd databsae. If it's
    a new database, fully create and skip migrations.
    """

    if database_exists(settings.SQLALCHEMY_DATABASE_URI):
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
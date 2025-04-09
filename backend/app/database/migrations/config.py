from alembic.config import Config

from settings import BASE_DIR, settings

alembic_cfg = Config()
alembic_cfg.set_main_option('script_location', f"{BASE_DIR}/app/database/migrations")
alembic_cfg.set_main_option('sqlalchemy.url', settings.SQLALCHEMY_DATABASE_URI)

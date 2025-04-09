from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from settings import settings

sync_engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI,
    pool_pre_ping=True,
    pool_size=10,
)
sync_session = sessionmaker(
    bind=sync_engine,
    autocommit=False,
    autoflush=False,
    future=True,
)


def get_sync_db() -> Session:
    with sync_session.begin() as sess:
        yield sess
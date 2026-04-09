from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.core.config import settings


class Database:
    """Database connection class."""
    def __init__(self):
        self._engine = create_engine(
            url=settings.DB_URL,
            echo=True,
            pool_size=settings.DB_POOL_SIZE,
            max_overflow=settings.DB_MAX_OVERFLOW,
            pool_timeout=settings.DB_POOL_TIMEOUT,
            pool_recycle=settings.DB_POOL_RECYCLE,
            pool_pre_ping=True,
        )

    @property
    def engine(self):
        return self._engine

    def create_db_and_tables(self) -> None:
        SQLModel.metadata.create_all(self.engine)

    def get_session_conn(self) -> Generator[Session, None, None]:
        with Session(self.engine) as session:
            yield session


db = Database()

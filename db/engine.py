from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


def create_new_async_engine(url: URL | str) -> AsyncEngine:
    return create_async_engine(url=url, echo=True, pool_pre_ping=True)


def proceed_schemas(engine: AsyncEngine, metadata) -> None:
    with engine.connect() as conn:
        conn.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, class_=AsyncSession)

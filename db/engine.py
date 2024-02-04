from sqlalchemy.engine import URL
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


def create_new_async_engine(url: URL | str) -> AsyncEngine:
    return create_async_engine(url=url, echo=True, encoding='utf-8', pool_pre_ping=True)


def proceed_schemas(session: AsyncSession, metadata) -> None:
    with session.begin():
        session.run_sync(metadata.create_all)


def get_session_maker(engine: AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, class_=AsyncSession)

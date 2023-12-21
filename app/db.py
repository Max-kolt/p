from sqlalchemy import MetaData, Table, create_engine, inspect, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from config import DB_HOST, DB_NAME, DB_PORT, DB_USER, DB_PASSWORD
# from models import load_models

from typing import AsyncGenerator
from fastapi import Depends

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

metadata = MetaData()


async def load_db():
    async with engine.connect() as conn:
        global metadata
        await conn.run_sync(
            lambda sync_conn: metadata.reflect(bind=sync_conn)
        )

        # await load_models(conn, metadata)


async def get_table(name: str) -> AsyncGenerator[Table, None]:
    async with engine.connect() as conn:
        table = await conn.run_sync(
            # lambda sync_conn: inspect(sync_conn).get_table_names()
            lambda sync_conn: Table(name, metadata, autoload_with=sync_conn)
        )
        while True:
            yield table


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def test():
    await load_db()
    tables = get_table('users')
    print(await tables.__anext__())


if __name__ == '__main__':
    import asyncio
    asyncio.run(test())


from sqlalchemy import update, delete, insert, Table
from sqlalchemy.future import select
from db import async_session_maker


class BaseRepo:
    model: Table

    @classmethod
    async def create(cls, **kwargs):
        model: Table = await cls.model.__anext__()
        async with async_session_maker() as session:
            to_exec = model.insert().values(**kwargs)
            await session.execute(to_exec)
            await session.commit()
            return True

    @classmethod
    async def get_all(cls):
        model = await cls.model.__anext__()
        async with async_session_maker() as session:
            query = select(model)
            return (await session.execute(query)).scalars().all()


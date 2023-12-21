from .base_repo import BaseRepo
from db import get_table, async_session_maker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select, Table, select
# from models.models import User


class UserRepository(BaseRepo):
    model = get_table('users')

    async def get_by_username_or_email(self, username: str = None, email: str = None):
        model = await self.model.__anext__()
        session: AsyncSession = async_session_maker()
        query = Select

        if username:
            query = select(model).where(model.c.username == username)
        elif email:
            query = select(model).where(model.c.email == email)

        result = await session.execute(query)

        await session.close()
        return result.first()

    async def get_experience(self, username: str = None, email: str = None):
        pass

    async def get_likes(self, username: str = None, email: str = None):
        pass

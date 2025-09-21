from sqlalchemy import select, insert, update, create_engine
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.base.model import Base
from src.core.db.dependence import SessionDI


class BaseDAO:
    def __init__(self, session: SessionDI, model: Base | None = None):
        self.session: AsyncSession = session
        self.model: Base | None = model

    async def find_by_id(self, model_id: int):
        q = select(self.model).filter_by(id=model_id)
        result = await self.session.execute(q)
        return await result.scalar_one_or_none()

    async def find_one_or_none(self, **kwargs):
        q = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(q)
        return result.scalar_one_or_none()

    async def find_all(self, **kwargs):
        q = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(q)
        return result.scalars().all()

    async def create(self, **data):
        q = insert(self.model).values(**data)
        await self.session.execute(q)
        await self.session.commit()

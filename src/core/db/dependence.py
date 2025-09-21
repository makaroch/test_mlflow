from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.db.connection import get_db

SessionDI = Annotated[AsyncSession, Depends(get_db)]

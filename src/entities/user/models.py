from datetime import datetime
from uuid import uuid4

from sqlalchemy import String, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base.model import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    pwd: Mapped[str] = mapped_column(String(255), nullable=False)
    date_create: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    projects: Mapped[list["UserProjectModel"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

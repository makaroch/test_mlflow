from datetime import datetime
from uuid import uuid4

from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base.model import Base
from src.entities.user.models import UserModel


class ProjectModel(Base):
    __tablename__ = "projects"

    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid4())
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    creator: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"))
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    network_docker: Mapped[str] = mapped_column(String(255))

    users: Mapped[list["UserProjectModel"]] = relationship(
        back_populates="project", cascade="all, delete-orphan"
    )


class RoleModel(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)


class UserProjectModel(Base):
    __tablename__ = "users_projects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(36), ForeignKey("users.id"))
    project_id: Mapped[str] = mapped_column(String(36), ForeignKey("projects.id"))
    role: Mapped[str] = mapped_column(String(50), ForeignKey("roles.name"))

    user: Mapped[UserModel] = relationship(back_populates="projects")
    project: Mapped[ProjectModel] = relationship(back_populates="users")
    role_rel: Mapped[RoleModel] = relationship()

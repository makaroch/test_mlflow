from starlette_admin.contrib.sqla.view import ModelView

from src.entities.progect.models import ProjectModel, RoleModel, UserProjectModel

prog_view = ModelView(ProjectModel)

role_view = ModelView(RoleModel)
user_project_view = ModelView(UserProjectModel)
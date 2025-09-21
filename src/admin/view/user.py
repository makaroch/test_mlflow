from starlette_admin.contrib.sqla.view import ModelView

from src.entities.user.models import UserModel

user_view = ModelView(UserModel)

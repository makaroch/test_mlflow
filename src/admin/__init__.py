from starlette_admin.contrib.sqla import Admin

from src.admin.view.prog import prog_view, role_view, user_project_view
from src.admin.view.user import user_view
from src.core.db.connection import engine

admin = Admin(engine, title="Mlflow Proxy Admin")


def get_admin() -> Admin:
    views = [
        prog_view,
        role_view,
        user_project_view,
        user_view,
    ]
    for view in views:
        admin.add_view(view)
    return admin
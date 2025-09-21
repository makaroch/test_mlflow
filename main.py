import os

from fastapi import FastAPI, Request, Depends, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
import httpx

from src.admin import get_admin
from src.api import get_api_router

app = FastAPI()

admin = get_admin()

admin.mount_to(app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(get_api_router())

MLFLOW_URL = os.getenv("MLFLOW_URL", "http://mlflow:5000")
USER_ROLES = {
    "user1": "editor",
    "user2": "admin",
}


def get_user_role(token: str = None):
    if token in USER_ROLES:
        return USER_ROLES[token]
    raise HTTPException(status_code=401, detail="Unauthorized")


# @app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
# async def proxy(path: str, request: Request, role: str = Depends(get_user_role)):
#     method = request.method
#
#     if method == "DELETE" and role != "admin":
#         raise HTTPException(status_code=403, detail="Forbidden: delete not allowed")
#     if method in ("POST", "PUT", "PATCH") and role not in ("editor", "admin"):
#         raise HTTPException(status_code=403, detail="Forbidden: write not allowed")
#
#     async with httpx.AsyncClient(follow_redirects=True) as client:
#         mlflow_response = await client.request(
#             method,
#             f"{MLFLOW_URL}/{path}",
#             headers={k: v for k, v in request.headers.items() if k.lower() != "host"},
#             content=await request.body(),
#         )
#
#     return Response(
#         content=mlflow_response.content,
#         status_code=mlflow_response.status_code,
#         headers=dict(mlflow_response.headers),
#         media_type=mlflow_response.headers.get("content-type")
#     )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

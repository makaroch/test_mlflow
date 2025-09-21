from fastapi import APIRouter

api_router = APIRouter(
    prefix="/api",
    tags=["api"],
)


def get_api_router():
    routers = [

    ]

    for router in routers:
        api_router.include_router(router)

    return api_router

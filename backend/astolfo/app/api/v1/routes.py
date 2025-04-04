from fastapi import APIRouter
from fastapi.routing import APIRoute

from api.v1 import user, company, plan, home, tasks, signature

api_v1_router = APIRouter()
api_v1_router.include_router(
    company.router, prefix="/company", tags=["Company"]
)

api_v1_router.include_router(
    user.router, prefix="/user", tags=["User"]
)

api_v1_router.include_router(
    signature.router, prefix="/signature", tags=["Signature"]
)

api_v1_router.include_router(
    plan.router, prefix="/plan", tags=["Plan"]
)

api_v1_router.include_router(
    home.router, prefix="/home", tags=["Home"]
)
api_v1_router.include_router(
    tasks.router, prefix="/tasks", tags=["Tasks"]
)



for route in api_v1_router.routes:
    if isinstance(route, APIRoute) and not route.operation_id:
        route.operation_id = route.name
from api.v1.routes import v1_router
from fastapi import APIRouter

api_router = APIRouter(prefix="/api", tags=["api"])

routers = [
    v1_router,
]

for router in routers:
    router.tags.append("api")
    api_router.include_router(router)

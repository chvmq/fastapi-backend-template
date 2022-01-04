from fastapi import APIRouter

from db.base import database
from endpoints.auth import router as auth_router


api_router = APIRouter(prefix="/api")
api_router.include_router(auth_router)


@api_router.on_event("startup")
async def startup():
    await database.connect()

@api_router.on_event("shutdown")
async def shutdown():
    await database.disconnect()


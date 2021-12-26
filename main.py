from uvicorn import run
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import (
    SITE_PORT,
    SITE_HOST,
    PROJECT_TITLE,
)
from db.base import database


app = FastAPI(title=PROJECT_TITLE)
app.add_middleware(
    CORSMiddleware,
    allow_origins="origins",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    run(
        "main:app",
        port=SITE_PORT,
        host=SITE_HOST,
        reload=True,
        forwarded_allow_ips="*",
    )


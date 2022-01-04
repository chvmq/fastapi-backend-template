from fastapi import APIRouter


router = APIRouter()


@router.get("/login")
async def login():
    return {"test": "test"}

@router.get("/register")
async def register():
    return {"register": "register"}


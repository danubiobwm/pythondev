from fastapi import APIRouter

user_router = APIRouter()

@user_router.get("/test")
async def teste():
    return {"message": "User test endpoint is working!"}
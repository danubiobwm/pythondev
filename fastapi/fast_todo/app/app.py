from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.user_model import User
from models.todo_model import Todo
from api.api_v1.router import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.on_event("startup")
async def app_init():
    cliente_db = AsyncIOMotorClient(
        settings.MONGO_CONNECTION_STRING).todoapp

    await init_beanie(
        database = cliente_db,
        document_models = [
            User,
            Todo
        ]
    )

app.include_router(
    router,
    prefix=settings.API_V1_STR,
)
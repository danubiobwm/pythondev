from fastapi import APIRouter
from schemas.todo_schema import TodoCreate, TodoUpdate, TodoDetail
from models.user_model import User
from api.dependencies.user_deps import get_current_user


todo_router = APIRouter()

@todo_router.get("/", summary="List all todos", response_model=TodoDetail)
async def List(current_user: User = Depends(get_current_user)):
    pass  # Implementation for listing todos

from fastapi import APIRouter, Depends
from schemas.todo_schema import TodoCreate, TodoDetail
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from services.todo_service import TodoService
from models.todo_model import Todo
from typing import List


todo_router = APIRouter()

@todo_router.get("/", summary="List all todos", response_model=TodoDetail)
async def List(current_user: User = Depends(get_current_user)):
    """
    List all todos for the current user.
    """
    return await TodoService.list_todos(current_user)

@todo_router.post("/create", summary="Create a new todo", response_model=TodoDetail)
async def Create(data: TodoCreate, current_user: User = Depends(get_current_user)):
    """
    Create a new todo for the current user.
    """
    return await TodoService.create_todo(current_user, data)
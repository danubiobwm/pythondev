from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from schemas.todo_schema import TodoCreate, TodoDetail, TodoUpdate
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from services.todo_service import TodoService
from models.todo_model import Todo
from typing import List


todo_router = APIRouter()

@todo_router.get("/", summary="List all todos", response_model=List[TodoDetail])
async def List(current_user: User = Depends(get_current_user)):
    """
    List all todos for the current user.
    """
    return await TodoService.list_todos(current_user)

@todo_router.post("/create", summary="Create a new todo", response_model=TodoDetail)
async def Create(data: TodoCreate, current_user: User = Depends(get_current_user)):
    return await TodoService.create_todo(current_user, data)

@todo_router.get("/{todo_id}", summary="Get todo details", response_model=TodoDetail)
async def Detail(todo_id: UUID, current_user: User = Depends(get_current_user)):
    todo = await TodoService.detail(current_user, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    return todo

@todo_router.put("/{todo_id}", summary="Update a todo", response_model=TodoDetail)
async def Update(todo_id: UUID, data: TodoUpdate, current_user: User = Depends(get_current_user)):
    return await TodoService.update_todo(current_user, todo_id, data)

@todo_router.delete("/{todo_id}", summary="Delete a todo")
async def Delete(todo_id: UUID, current_user: User = Depends(get_current_user)):
    success = await TodoService.delete_todo(current_user, todo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Todo not found or does not belong to the user")
    return {"detail": "Todo deleted successfully"}

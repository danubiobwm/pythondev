from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID
from datetime import datetime

class TodoCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., title="Description of the todo item", min_length=3, max_length=1000)
    status: Optional[bool] = False


class TodoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[bool]

class TodoDetail(BaseModel):
    todo_id: UUID
    status: bool
    title: str
    description: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


from typing import  Optional
from datetime import datetime
from uuid import uuid4, UUID
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from pydantic import BaseModel, Field
from .user_model import User


class Todo(Document):
    todo_id: UUID = Field(default_factory=uuid4, unique=True)
    status: bool = Field(default=True)
    title: Indexed(str)
    description: Indexed(str)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner: Link[User]

    def __repr__(self) -> str:
        return f"<Todo f{self.title}>"

    def __str__(self) -> str:
        return f"<Todo f{self.title}>"

    def __hash__(self) -> int:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Todo):
          return self.todo_id == other.todo_id
        return False

    @before_event([Replace, Insert])
    def sync_updated_at(self):
        self.updated_at = datetime.utcnow()
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService


auth_router = APIRouter()
@auth_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        username=form_data.username,
        password=form_data.password
    )

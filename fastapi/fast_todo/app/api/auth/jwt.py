from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.security import create_access_token

auth_router = APIRouter()

@auth_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Use email ou username conforme sua estratégia
    user = await UserService.authenticate(
        email=form_data.username,  # ou username=form_data.username
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_access_token(user.user_id, is_refresh=True),
        "token_type": "bearer"
    }
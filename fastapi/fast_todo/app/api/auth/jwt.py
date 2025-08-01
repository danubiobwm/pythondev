from fastapi import APIRouter, Depends, HTTPException, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_service import UserService
from core.security import  create_access_token, create_refresh_token
from schemas.auth_schema import TokenSchema
from schemas.user_schema import UserDetail
from models.user_model import User
from api.dependencies.user_deps import get_current_user
from pydantic import ValidationError
from core.config import settings
from schemas.auth_schema import TokenPayload
from jose import jwt



auth_router = APIRouter()

@auth_router.post('/login', summary='Cria Access Token e Refresh Token', response_model=TokenSchema)
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email=data.username,
        password=data.password
    )
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='E-mail ou Senha estão incorretos'
        )

    return {
        "access_token" : create_access_token(usuario.user_id),
        "refresh_token": create_refresh_token(usuario.user_id),
        "token_type": "bearer"
    }

@auth_router.post('/test-token', summary='Testando o Token', response_model=UserDetail)
async def test_token(user: User = Depends(get_current_user)):
    return user

@auth_router.post('/refresh', summary='Refresh Token', response_model=TokenSchema)
async def refresh_token(refresh_token: str = Body(...)):
    try:
        payload = jwt.decode(
            refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            algorithms=[settings.ALGORITHM]  # Fixed: algorithms should be a list
        )
        token_data = TokenPayload(**payload)

        # Verify token type is refresh
        if token_data.type != "refresh":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Invalid token type",
                headers={'WWW-Authenticate': 'Bearer'}
            )

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Token expired",
            headers={'WWW-Authenticate': 'Bearer'}
        )
    except (jwt.JWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Token inválido',  # Fixed: changed 'details' to 'detail'
            headers={'WWW-Authenticate': 'Bearer'}
        )

    user = await UserService.get_user_by_id(token_data.sub)

    if not user:  # Fixed: changed 'User' to 'user' (lowercase)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Não foi possível encontrar o usuário',  # Fixed: changed 'details' to 'detail'
            headers={'WWW-Authenticate': 'Bearer'}
        )

    return {
        "access_token": create_access_token(user.user_id),
        "refresh_token": create_refresh_token(user.user_id),
        "token_type": "bearer"  # Added for consistency with login response
    }
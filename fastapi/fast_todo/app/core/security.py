from passlib.context import CryptContext
from typing import Union, Any
from datetime import datetime, timedelta
from jose import jwt
from core.config import settings

password_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def get_password_hash(password: str) -> str:  # Nome alterado
    return password_context.hash(password)

def verify_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password)

def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None, is_refresh: bool = False) -> str:
    if expires_delta is not None:
        expires_at = datetime.utcnow() + expires_delta
    else:
        expires_at = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES if is_refresh
                   else settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )

    payload = {
        "exp": expires_at,
        "sub": str(subject),
        "type": "refresh" if is_refresh else "access"
    }

    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
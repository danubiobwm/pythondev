import email
from typing import Optional
from schemas.user_schema import UserAuth
from models.user_model import UserModel
from core.security import get_password_hash, verify_password


class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
        usuario = UserModel(
            username=user.username,
            email=user.email,
            hash_password=get_password_hash(user.password),
        )
        await usuario.save()
        return usuario

    @staticmethod
    async def get_user_by_email(email: str) -> Optional[UserModel]:
        user = await UserModel.find_one(UserModel.email == email)
        return user

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[UserModel]:
        user = await UserModel.get_user_by_email(email=email)
        if not user:
            return None
        if not verify_password(
            password=password, hash_password=UserModel.hash_password
        ):
            return None
        return user

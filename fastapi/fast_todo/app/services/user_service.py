import email
from schemas.user_schema import UserAuth
from models.user_model import UserModel
from core.security import get_password_hash

class UserService:
    @staticmethod
    async def create_user(user: UserAuth):
      usuario = UserModel(
        username=user.username,
        email=user.email,
        hash_password=get_password_hash(user.password)
      )
      await usuario.save()
      return usuario


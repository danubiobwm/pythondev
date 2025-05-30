import email
from schemas.user_schema import UserAuth
from models.user_model import UserModel

class UserService:
    @staticmethod
    def create_user(user: UserAuth):
      usuario = UserModel(
        username=user.username,
        email=user.email,
        hash_password=user.password
      )




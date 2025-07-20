from pydantic import BaseModel
from uuid import UUID

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: None | UUID = None
    exp: None | int = None
from pydantic import BaseModel

class JogadorModels(BaseModel):
    jogador_nome: str
    jogador_idade: int
    jogador_time: str

    class Config:
        orm_mode = True
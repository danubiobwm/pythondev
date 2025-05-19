from fastapi import APIRouter
from config.database import db
from models.jogador_models import JogadorModels
from schemas.jogador_schema import jogadorEntity, ListaJogadoresEntity

jogador_router = APIRouter()

@jogador_router.get("/")
async def inicio():
    return {"message": "API de Jogadores"}

#lista jogadores
@jogador_router.get("/jogadores")
async def lista_jogadores():
    return ListaJogadoresEntity(db.db_play.jogador.find())


#inserir jogador
@jogador_router.post("/jogadores")
async def cadastra_jogador(jogador: JogadorModels):
    db.db_play.jogador.insert_one(dict(jogador))
    return jogadorEntity(jogador)


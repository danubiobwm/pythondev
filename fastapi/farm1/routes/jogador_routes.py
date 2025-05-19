from fastapi import APIRouter
from config.database import db
from models.jogador_models import JogadorModels
from schemas.jogador_schema import jogadorEntity, ListaJogadoresEntity
from bson import ObjectId

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

#detalhes jogador
@jogador_router.get("/jogadores/{jogador_id}")
async def detalhes_jogador(jogador_id):
    jogador = db.db_play.jogador.find_one({"_id": ObjectId(jogador_id)})
    if jogador:
        return jogadorEntity(jogador)
    return {"error": "Jogador não encontrado"}

#Atualiza jogador
@jogador_router.put("/jogadores/{jogador_id}")
async def atualiza_jogador(jogador_id, jogador: JogadorModels):
    db.db_play.jogador.update_one({"_id": ObjectId(jogador_id)}, {"$set": dict(jogador)})
    return jogadorEntity(jogador)

#Deleta jogador
@jogador_router.delete("/jogadores/{jogador_id}")
async def deleta_jogador(jogador_id):
    db.db_play.jogador.delete_one({"_id": ObjectId(jogador_id)})
    return {"message": "Jogador deletado com sucesso"}
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

jogadores ={
    "1": {
        "nome": "Lucas",
        "idade": 25,
        "posicao": "Atacante"
    },
    "2": {
        "nome": "João",
        "idade": 30,
        "posicao": "Meio-campo"
    },
    "3": {
        "nome": "Maria",
        "idade": 28,
        "posicao": "Defensora"
    }
}

# base jogadores
class Jogador(BaseModel):
    nome: str
    idade: int
    posicao: str

@app.get("/")
async def inicio():
    return jogadores

@app.get("/jogador/{id}")
async def jogador(id: str):
    if id in jogadores:
        return jogadores[id]
    else:
        return {"erro": "Jogador não encontrado"}


#jogador query
@app.get("/jogador")
async def jogador_query(nome: str):
    for id, jogador in jogadores.items():
        if jogador["nome"] == nome:
            return {id: jogador}
    return {"erro": "Jogador não encontrado"}

# post jogador
@app.post("/jogador")
async def adicionar_jogador(id: int, jogador: Jogador):
    if str(id) in jogadores:
        return {"erro": "Jogador já existe"}
    else:
        jogadores[str(id)] = jogador.dict()
        return {"mensagem": "Jogador adicionado com sucesso", "jogador": jogadores[str(id)]}

# put jogador
@app.put("/jogador/{id}")
async def atualizar_jogador(id: str, jogador: Jogador):
    if id in jogadores:
        jogadores[id] = jogador.dict()
        return {"mensagem": "Jogador atualizado com sucesso", "jogador": jogadores[id]}
    else:
        return {"erro": "Jogador não encontrado"}


# delete jogador
@app.delete("/jogador/{id}")
async def deletar_jogador(id: str):
    if id in jogadores:
        del jogadores[id]
        return {"mensagem": "Jogador deletado com sucesso"}
    else:
        return {"erro": "Jogador não encontrado"}

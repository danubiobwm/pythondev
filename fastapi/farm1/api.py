from fastapi import FastAPI
from routes.jogador_routes import jogador_router

app= FastAPI()

app.include_router(jogador_router)
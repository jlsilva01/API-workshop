""" Arquivo principal do programa."""

from fastapi import FastAPI

app = FastAPI()

# criar uma rotas
@app.get("/") # request
def ola_mundo(): # response
    return {"Ola": "Mundo"} # mensagem de retorno
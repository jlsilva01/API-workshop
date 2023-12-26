""" Arquivo principal do programa."""

from fastapi import FastAPI
from typing import Dict, List

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um smartphone top de linha.",
        "preco": 1500.00
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um notebook gamer.",
        "preco": 3500.00
    },
    {
        "id": 3,
        "nome": "Tablet",
        "descricao": "Um tablet intermediario.",
        "preco": 1200.00
    }
]

@app.get("/")
def ola_mundo():
    """ Função que retorna uma mensagem de olá mundo."""
    return {"Ola": "Mundo"}

@app.get("/produtos")
def listar_produtos():
    """ Função que retorna a lista de produtos."""
    return produtos

@app.get("/produtos/{id}")
def buscar_produto(id: int):
    """ Função que retorna um produto."""
    for produto in produtos:
        if produto["id"] == id:
            return produto
    return {"Status": 404, "Mensagem": "Produto não encontrado."}
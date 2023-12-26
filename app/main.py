""" Arquivo principal do programa."""
from fastapi import FastAPI
from typing import Dict, List
from .schema import ProdutosSchema
from .data import Produtos

app = FastAPI()
lista_de_produtos = Produtos()

@app.get("/")
def ola_mundo():
    """ Função que retorna uma mensagem de olá mundo."""
    return {"Ola": "Mundo"}

@app.get("/produtos", response_model=List[ProdutosSchema])
def listar_produtos():
    """ Função que retorna a lista de produtos."""
    return lista_de_produtos.listar_produtos()

@app.get("/produtos/{id}", response_model=List[ProdutosSchema])
def buscar_produto(id: int):
    """ Função que retorna um produto."""
    return lista_de_produtos.buscar_produto(id)
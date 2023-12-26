from pydantic import BaseModel

class ProdutosSchema(BaseModel):
    """ Classe que representa o schema de um produto."""
    id: int
    nome: str
    descricao: str
    preco: float
from pydantic import BaseModel
from typing import List, Optional


class Biblioteca(BaseModel):
    nome: str
    ano_de_publicacao: int
    autor: str
    descricao: Optional[str] = None
    generos: List[str]
    

    def __str__(self):
        return f'{self.nome}, {self.descricao}, {self.generos}'
    

livro = Biblioteca(
    nome="Quincas Borba",
    ano_de_publicacao = 1891,
    autor = "Machado de Assis",
    descricao = None,
    generos = ["Aventura", "Drama", "Romance"]
)

print(livro)

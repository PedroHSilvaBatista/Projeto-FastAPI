from pydantic import BaseModel
from typing import List, Union


class Biblioteca(BaseModel):
    _nome: str
    _ano_de_publicacao: int
    _autor: str
    _descricao: Union[str, None] = None
    _generos: List[str]
    
    def __str__(self):
        return f'{self._nome}, {self._descricao}, {self._generos}'
    
    @property
    def get_nome(self):
        return self._nome

    @property
    def get_ano_de_publicacao(self):
        return self._ano_de_publicacao
    
    @property
    def get_autor(self):
        return self._autor

    @property
    def get_descricao(self):
        if self._descricao is not None:
            return self._descricao
        return None

    @property
    def get_generos(self):
        return self._generos

    

livro = Biblioteca(
    nome="Quincas Borba",
    ano_de_publicacao = 1891,
    autor = "Machado de Assis",
    descricao = None,
    generos = ["Aventura", "Drama", "Romance"]
)

print(livro)

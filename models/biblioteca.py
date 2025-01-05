from pydantic import BaseModel
from typing import List, Union

class Biblioteca(BaseModel):
    nome: str
    ano_de_publicacao: int
    autor: str
    descricao: Union[str, None] = None
    generos: List[str]
    
    def __str__(self):
        return f'{self.nome}, {self.descricao}, {self.generos}'
    
    @property
    def get_nome(self):
        return self.nome

    @property
    def get_ano_de_publicacao(self):
        return self.ano_de_publicacao
    
    @property
    def get_autor(self):
        return self.autor

    @property
    def get_descricao(self):
        if self.descricao is not None:
            return self.descricao
        return None

    @property
    def get_generos(self):
        return self.generos
    
    def serializar_objeto(self):
        return {
            "nome": self.nome,
            "ano_de_publicacao": self.ano_de_publicacao,
            "autor": self.autor,
            "descricao": self.descricao,
            "generos": self.generos
        }

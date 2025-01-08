# Bibliotecas utilizadas na construção da classe
from pydantic import BaseModel
from typing import List, Union

class Livro(BaseModel):
    # Atributos da classe Livro
    nome: str
    ano_de_publicacao: int
    autor: str
    descricao: Union[str, None] = None
    generos: List[str]
    
    def __str__(self) -> str:
        """Função que permite exibir uma representação do objeto em formato de string. Retorna os atributos do objeto"""
        return f'{self.nome}, {self.ano_de_publicacao}, {self.autor}, {self.descricao}, {self.generos}'
    
    @property
    def get_nome(self) -> str:
        """Função que retorna o nome do livro"""
        return self.nome

    @property
    def get_ano_de_publicacao(self) -> int:
        """Função que retorna o ano de publicação do livro"""
        return self.ano_de_publicacao
    
    @property
    def get_autor(self) -> str:
        """Função que retorna o nome do autor do livro"""
        return self.autor

    @property
    def get_descricao(self) -> Union[str, None]:
        """Função que retorna a descrição do livro caso o usuário tenha adicionado uma descrição"""
        if self.descricao is not None:
            return self.descricao
        return None

    @property
    def get_generos(self) -> list:
        """Função que retorna os gêneros do livro em formato de uma lista"""
        return self.generos
    
    def serializar_objeto(self) -> dict:
        """Função que permite serializar o objeto em um formato JSON. Retorna um dicionário"""
        return {
            "nome": self.nome,
            "ano_de_publicacao": self.ano_de_publicacao,
            "autor": self.autor,
            "descricao": self.descricao,
            "generos": self.generos
        }

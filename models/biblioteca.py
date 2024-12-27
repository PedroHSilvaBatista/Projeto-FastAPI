import os
from pydantic import BaseModel
from typing import List, Union

diretorio_atual = os.path.dirname(__file__)
caminho_dados = os.path.join(diretorio_atual, '..', 'data', 'livros.json')


class Biblioteca(BaseModel):
    # Faça com que os livros instanciados sejam enviados ao banco de dados
    # Faça com que o catálogo seja preenchido com os livros que estão no banco de dados
    catalogo = []

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
    
    def adicionar_ao_catalogo(self):
        Biblioteca.catalogo.append(self)

    def serializar_objeto(self):
        return {
            "nome": self.nome,
            "ano_de_publicacao": self.ano_de_publicacao,
            "autor": self.autor,
            "descricao": self.descricao,
            "generos": self.generos
        }

 
livro = Biblioteca(
    nome="Quincas Borba",
    ano_de_publicacao= 1891,
    autor= "Machado de Assis",
    descricao= None,
    generos= ["Aventura", "Drama", "Romance"]
).adicionar_ao_catalogo()

livro1 = Biblioteca(
    nome= "Memórias Póstumas de Brás Cubas",
    ano_de_publicacao= 1881,
    autor= "Machado de Assis",
    descricao= "Memórias Póstumas de Brás Cubas é um romance escrito por Machado de Assis, desenvolvido em princípio como folhetim, de março a dezembro de 1880, na Revista Brasileira, para, no ano seguinte, ser publicado como livro, pela então Tipografia Nacional como Memorias Posthumas de Braz Cubas.",
    generos= ["Romance", "Ficção"]
).adicionar_ao_catalogo()

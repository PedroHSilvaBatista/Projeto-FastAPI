import os, json
from pydantic import BaseModel
from typing import List, Union

diretorio_atual = os.path.dirname(__file__)
caminho_dados = os.path.join(diretorio_atual, '..', 'data', 'livros.json')


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


lista = []

livro = Biblioteca(
    nome="Quincas Borba",
    ano_de_publicacao= 1891,
    autor= "Machado de Assis",
    descricao= None,
    generos= ["Aventura", "Drama", "Romance"]
).serializar_objeto()

livro1 = Biblioteca(
    nome= "Memórias Póstumas de Brás Cubas",
    ano_de_publicacao= 1881,
    autor= "Machado de Assis",
    descricao= "Memórias Póstumas de Brás Cubas é um romance escrito por Machado de Assis, desenvolvido em princípio como folhetim, de março a dezembro de 1880, na Revista Brasileira, para, no ano seguinte, ser publicado como livro, pela então Tipografia Nacional como Memorias Posthumas de Braz Cubas.",
    generos= ["Romance", "Ficção"]
).serializar_objeto()

livro2 = Biblioteca(
    nome= "Memórias de um Sargento de Milícias",
    ano_de_publicacao= 1853,
    autor= "Manuel Antônio de Almeida",
    descricao= None,
    generos= ["Romance", "Ficção", "Sátira"]
).serializar_objeto()

livro3 = Biblioteca(
    nome= "Dois Irmãos",
    ano_de_publicacao= 2000,
    autor= "Miltom Hatoum",
    descricao= "Neste romance de intensa dramaticidade, Milton Hatoum narra a história de dois irmãos gêmeos - Yaqub e Omar - e suas relações com a mãe, o pai, a irmã e, de outro lado, com a empregada da família e seu filho, um menino cuja infância é moldada justamente por esta condição: ser o filho da empregada.",
    generos= ["Romance", "Drama"]
).serializar_objeto()

livro4 = Biblioteca(
    nome= "Campo Geral",
    ano_de_publicacao= 1964,
    autor= "João Guimarães Rosa",
    descricao= "O que fala o livro Campo Geral? O livro “Campo Geral”, publicado em 1964 por Guimarães Rosa, tem 136 páginas e narra a história do menino Miguilim, que vive sua infância em meio à natureza, em Minas Gerais. A novela é narrada pela perspectiva do próprio Miguilim e se passa entre 1889 e 1930.",
    generos= ["Fição"]
).serializar_objeto()

lista.append(livro)
lista.append(livro1)
lista.append(livro2)
lista.append(livro3)
lista.append(livro4)

with open(caminho_dados, 'w', encoding='utf-8') as arquivo:
    json.dump(lista, arquivo, indent=4, ensure_ascii=False)

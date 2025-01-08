# Bibliotecas e framework utilizados
import os, json
from typing import Union
from fastapi import FastAPI
from models.biblioteca import Livro

# Caminhos com suas respectivas rotas
diretorio_atual = os.path.dirname(__file__)
caminho_dados = os.path.join(diretorio_atual, 'data', 'livros.json')


def pegar_dados_do_banco_de_dados() -> list:
    """Esta função traz todos os livros cadastrados no banco de dados e retorna os dados em formato de lista"""
    with open(caminho_dados, 'r', encoding='utf-8') as arquivo_leitura:
        dados = json.load(arquivo_leitura)
    return dados

# Instância do objeto FastAPI(Framework utilizado para a construção da API)
app = FastAPI()

# Método GET
@app.get('/')
def listar_livros():
    livros = pegar_dados_do_banco_de_dados()
    return livros

#Método POST
@app.post('/livro')
def cadastrar_novo_livro(livro: dict):
    dados = pegar_dados_do_banco_de_dados()

    # Estrutura que faz a busca do livro solicitado para que não haja cópias de livros
    encontrou_livro = False
    for livro in dados:
        if livro["nome"] == livro:
            encontrou_livro = True
            break
    
    # Resposta emitida caso o livro já esteja cadastrado
    if encontrou_livro:
        return "Livro já encontrado no registro"

    # Adição do livro ao banco de dados
    dados.append(livro)
    with open(caminho_dados, 'w', encoding='utf-8') as arquivo_adicao:
        json.dump(dados, arquivo_adicao, indent=4, ensure_ascii=False)

    # Resposta emitida caso o livro ainda não esteja cadastrado
    return {"status": "inserted"}

#Método PUT - Parâmetro utilizado: nome do livro que deseja-se alterar
@app.put("/livro/{nome_do_livro}")
def atualizar_livro(nome_do_livro: str, novo_livro: Union[dict, Livro]):
    dados = pegar_dados_do_banco_de_dados()

    # Estrutura que faz a busca do livro solicitado e altera o livro caso encontrado
    encontrou_livro = False
    for i in range(len(dados)):
        if dados[i]["nome"] == nome_do_livro:
            dados[i] = novo_livro
            encontrou_livro = True
            break
    
    # Resposta emitida caso o livro não seja encontrado
    if not encontrou_livro:
        return "Livro não encontrado"
    
    # Alteração do banco de dados
    with open(caminho_dados, 'w', encoding='utf-8') as arquivo_edicao:
        json.dump(dados, arquivo_edicao, indent=4, ensure_ascii=False)

    # Resposta emitida caso o livro seja encontrado
    return {"status": "edited", "updated_book": novo_livro}

#Método DELETE - Parâmetro utilizado: nome do livro que deseja-se excluir
@app.delete("/livro/remover/{nome_do_livro_remocao}")
def deletar_livro(nome_do_livro_remocao: str):
    dados = pegar_dados_do_banco_de_dados()

    # Estrutura que faz a busca do livro solicitado e exclui o livro caso encontrado
    encontrou_livro = False
    for i in range(len(dados)):
        if dados[i]["nome"] == nome_do_livro_remocao:
            dados.pop(i)
            encontrou_livro = True
            break

    # Resposta emitida caso o livro não seja encontrado
    if not encontrou_livro:
        return "Livro não encontrado"
    
    # Alteração do banco de dados
    with open(caminho_dados, 'w', encoding='utf-8') as arquivo_edicao:
        json.dump(dados, arquivo_edicao, indent=4, ensure_ascii=False)

    # Resposta emitida caso o livro seja encontrado
    return {"status": "deleted", "removed_book": nome_do_livro_remocao}

import os, json
from typing import Union
from fastapi import FastAPI
from models.biblioteca import Livro

diretorio_atual = os.path.dirname(__file__)
caminho_dados = os.path.join(diretorio_atual, 'data', 'livros.json')


def pegar_dados_do_banco_de_dados():
    with open(caminho_dados, 'r', encoding='utf-8') as arquivo_leitura:
        dados = json.load(arquivo_leitura)
    return dados


app = FastAPI()

@app.get('/')
def listar_livros():
    livros = pegar_dados_do_banco_de_dados()
    return livros

@app.post('/livro')
def cadastrar_novo_livro(livro: dict):
    dados = pegar_dados_do_banco_de_dados()

    encontrou_livro = False
    for livro in dados:
        if livro["nome"] == livro:
            encontrou_livro = True
            break

    if encontrou_livro:
        return "Livro já encontrado no registro"

    dados.append(livro)
    with open(caminho_dados, 'w', encoding='utf-8') as arquivo_adicao:
        json.dump(dados, arquivo_adicao, indent=4, ensure_ascii=False)

    return {"status": "inserted"}

@app.put("/livro/{nome_do_livro}")
def atualizar_livro(nome_do_livro: str, novo_livro: Union[dict, Livro]):
    dados = pegar_dados_do_banco_de_dados()

    encontrou_livro = False
    for i in range(len(dados)):
        if dados[i]["nome"] == nome_do_livro:
            dados[i] = novo_livro
            encontrou_livro = True
            break
    
    if not encontrou_livro:
        return "Livro não foi encontrado"
    
    with open(caminho_dados, 'w', encoding='utf-8') as arquivo_edicao:
        json.dump(dados, arquivo_edicao, indent=4, ensure_ascii=False)
    
    return {"status": "edited", "updated_book": novo_livro}

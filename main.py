import os, json
from fastapi import FastAPI

diretorio_atual = os.path.dirname(__file__)
caminho_dados = os.path.join(diretorio_atual, 'data', 'livros.json')


app = FastAPI()

@app.get('/')
def listar_livros():
    with open(caminho_dados, 'r', encoding='utf-8') as arquivo_leitura:
        dados = json.load(arquivo_leitura)
    return dados

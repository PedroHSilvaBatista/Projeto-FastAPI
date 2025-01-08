# Importações feitas
import os, json

# Respectivos caminhos utilizados
diretorio_atual = os.path.dirname(__file__)
caminho_dados = os.path.join(diretorio_atual, '..', 'data', 'livros.json') 


def encontrar_livro(nome_do_livro_de_busca: str) -> bool:
    """Esta função faz uma busca do livro solicitado ao banco de dados
    e retorna, por meio de um valor booleano, se encontrou o livro requisitado"""
    with open(caminho_dados, 'r', encoding='utf-8') as arquivo_leitura:
        dados = json.load(arquivo_leitura)
    
    encontrou_livro = False
    for livro in dados:
        if livro["nome"].replace(' ', '') == nome_do_livro_de_busca.replace(' ', ''):
            encontrou_livro = True
            break
    
    return encontrou_livro

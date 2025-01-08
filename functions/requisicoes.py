# Biblioteca utilizada 
import requests


def get() -> None:
    """Esta função realiza um método GET utilizando a API criada. Não possui retorno"""
    try:
        endpoint = 'http://localhost:8000/'
        response = requests.get(endpoint)

        if response.status_code == 200:
            dados = response.json()
            return dados
        else:
            print('Ocorreu um erro inesperado.')
    except requests.exceptions.ConnectionError as erro:
        print(f'Erro. Erro de conexão com a API: {erro}.')
    except Exception as erro_geral:
        print(f'Ocorreu um erro inesperados. Mensagem de erro {erro_geral}.')


def post(livro: dict) -> None:
    """Esta função realiza um método POST utilizando a API criada. Não possui retorno"""
    try:
        endpoint = 'http://localhost:8000/livro'
        response = requests.post(endpoint, json=livro)

        if response.status_code == 200:
            print('Livro cadastrado com sucesso!')
        else:
            print('Ocorreu um erro inesperado.')
    except requests.exceptions.ConnectionError as erro_conexao:
        print(f'Erro. Erro de conexção com a API: {erro_conexao}')
    except Exception as erro_geral:
        print(f'Ocorreu um errro inesperado. Mensagem de erro {erro_geral}')


def put(nome_do_livro: str, novo_livro: dict) -> None:
    """Esta função realiza um método PUT utilizando a API criada. Não Possui retorno"""
    try:
        endpoint = f'http://localhost:8000/livro/{nome_do_livro}'
        response = requests.put(endpoint, json=novo_livro)

        if response.status_code == 200:
            print('Livro alterado com sucesso!')
        else:
            print('Ocorreu um erro inesperado')
    except requests.exceptions.ConnectionError as erro_conexao:
        print(f'Erro. Erro de conexão com a API: {erro_conexao}')
    except Exception as erro_geral:
        print(f'Ocorreu um erro inesperado. Mensagem de erro {erro_geral}')


def delete(nome_do_livro_remocao: str) -> None:
    """Esta função realiza um método DELETE utilizando a API criada. Não possui retorno"""
    try:
        endpoint = f"http://localhost:8000/livro/remover/{nome_do_livro_remocao}"
        response = requests.delete(endpoint)

        if response.status_code == 200:
            print('Livro excluído com sucesso!')
        else:
            print('Ocorreu um erro inesperado')
    except requests.exceptions.ConnectionError as erro_conexao:
        print(f'Erro. Erro de conexão com a API: {erro_conexao}')
    except Exception as erro_geral:
        print(f'Ocorreu um erro inesperado. Mensagem de erro {erro_geral}')

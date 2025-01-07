import requests


def get():
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


def post(livro: dict):
    try:
        endpoint = 'http://localhost:8000/livro'
        response = requests.post(endpoint, json=livro)

        if response.status_code == 200:
            print('Livro cadastrado com sucesso!')
        else:
            print('Ocorreu um erro inesperado.')
    except requests.exceptions.ConnectionError as erro:
        print(f'Erro. Erro de conexção com a API: {erro}')
    except Exception as erro_geral:
        print(f'Ocorreu um errro inesperado. Mensagem de erro {erro_geral}')
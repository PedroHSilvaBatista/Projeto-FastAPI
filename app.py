from functions.menu import menu
from functions.requisicoes import get


def app():
    while True:
        menu()
        usuario_menu = input('Digite a opção desejada: ')

        match usuario_menu:
            case '1':
                print('Aqui estão todos os livros já cadastrados:')
                catalogo = get()
                print(catalogo)
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                print('Volte sempre :)')
                print('Encerrando o programa...')
                break
            case _:
                print('Por favor, digite uma opção válida')


if __name__ == '__main__':
    app()

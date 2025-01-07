from functions.menu import menu
from functions.requisicoes import get, post, put
from models.biblioteca import Livro


def app():
    while True:
        menu()
        usuario_menu = input('Digite a opção desejada: ')

        match usuario_menu:
            case '1':
                print('Aqui estão todos os livros já cadastrados:')
                print()
                catalogo = get()
                for livro in catalogo:
                    print(f"{livro["nome"]} ({livro["autor"]}) - {livro["ano_de_publicacao"]}")
            case '2':
                print('Para que possamos adicionar um novo livro à bilbioteca, é necessário primeiro preencher algumas informações importantes')
                try:
                    nome_do_livro = input('Digite o nome da obra que queira cadastrar: ')
                    ano_de_publicacao_do_livro = int(input('Digite o ano de publicação do livro: '))
                    nome_do_autor = input('Digite o nome do autor(a) do livro: ')

                    descricao_do_livro = input('Forneça uma descrição do livro (opcional, aperte Enter caso não queira adicionar uma descrição): ')
                    if descricao_do_livro == '':
                        descricao_do_livro = None

                    print('Forneça três gêneros que mais combinam com o livro selecionado')
                    lista_de_generos = []
                    for i in range(3):
                        lista_de_generos.append(input(f'{i+1}° Genêro: '))

                    livro_criado = Livro(
                        nome=nome_do_livro,
                        ano_de_publicacao=ano_de_publicacao_do_livro,
                        autor=nome_do_autor,
                        descricao=descricao_do_livro,
                        generos=lista_de_generos
                    ).serializar_objeto()

                    post(livro_criado)
                except ValueError:
                    print('Por favor, digite um valor inteiro quando for inserir a data de publicação do livro')
                except Exception:
                    print('Ocorreu um erro inesperado! Tente novamente mais tarde')
            case '3':
                print('Lista de livros cadastrados passíveis de alteração:')
                catalogo = get()
                for livro in catalogo:
                    print(f"{livro["nome"]} ({livro["autor"]}) - {livro["ano_de_publicacao"]}")

                try:
                    escolha_usuario_alteracao_de_livro = input('Nome do livro que deseja alterar: ').strip()
                    print('Para que possamos alterar um livro é necessário inserir todas as informações de um livro novamente')

                    nome_do_livro_alteracao = input(f'Digite o nome da obra que queira substituir {escolha_usuario_alteracao_de_livro}: ')
                    ano_de_publicacao_do_livro_alteracao = int(input('Digite o ano de publicação do livro: '))
                    nome_do_autor_alteracao = input('Digite o nome do autor(a) do livro: ')

                    descricao_do_livro_alteracao = input('Forneça uma descrição do livro (opcional, aperte Enter caso não queira adicionar uma descrição): ')
                    if descricao_do_livro_alteracao == '':
                            descricao_do_livro_alteracao = None

                    print('Forneça três gêneros que mais combinam com o livro')
                    lista_de_generos_alteracao = []
                    for i in range(3):
                        lista_de_generos_alteracao.append(input(f'{i+1}° Genêro: '))

                    novo_livro_por_alteracao = Livro(
                        nome=nome_do_livro_alteracao,
                        ano_de_publicacao=ano_de_publicacao_do_livro_alteracao,
                        autor=nome_do_autor_alteracao,
                        descricao=descricao_do_livro_alteracao,
                        generos=lista_de_generos_alteracao
                    ).serializar_objeto()

                    put(escolha_usuario_alteracao_de_livro, novo_livro_por_alteracao)
                except ValueError:
                    print('Por favor, digite um valor inteiro quando for inserir a data de publicação do livro')
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

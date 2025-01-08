# Funções e classes importadas
from functions.menu import menu
from functions.requisicoes import get, post, put, delete
from functions.encontrar_livro import encontrar_livro
from models.biblioteca import Livro


# Função principal do programa
def app():
    # Loop de controle do sistema
    while True:
        # Exibe o menu da aplicação
        menu()
        # Variável que armazena a escolha do usuário de acordo com o funcionalidade escolhida
        usuario_menu = input('Digite a opção desejada: ')

        match usuario_menu:
            case '1':
                # Funcionalidade que exibe todos os livros já cadastrados no sistema
                print('Aqui estão todos os livros já cadastrados:')
                print()
                # Variável que armazena os dados do banco de dados por meio da requisição GET à nossa API
                catalogo = get()
                for livro in catalogo:
                    print(f"{livro["nome"]} ({livro["autor"]}) - {livro["ano_de_publicacao"]}")
            case '2':
                # Funcionalidade que permite o usuário adicionar um novo livro ao banco de dados
                print('Para que possamos adicionar um novo livro à bilbioteca, é necessário primeiro preencher algumas informações importantes')

                # Tratamento de exceções para garantir que o usuário não preencha nenhum campo com o valor indevido
                try:
                    nome_do_livro = input('Digite o nome da obra que queira cadastrar: ')
                    # Variável de controle que verifica se o nome do livro sugerido já não se encontra no banco de dados
                    encontrou_livro_para_adicao = encontrar_livro(nome_do_livro)

                    # Caso o livro digitado ainda não esteja cadastrado o processo de adição continua
                    if not encontrou_livro_para_adicao:
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

                        # Função que envia o novo livro criado ao banco de dados por meio de um método POST pela nossa própria API
                        post(livro_criado)
                    else:
                        # Caso o livro já esteja cadastrado, a seguinte mensagem é emitida
                        print(f'O livro {nome_do_livro} já se encontra registrado no sistema. Tente adicionar outro livro')
                except ValueError:
                    print('Por favor, digite um valor inteiro quando for inserir a data de publicação do livro')
                except Exception:
                    print('Ocorreu um erro inesperado! Tente novamente mais tarde')
            case '3':
                # Funcionalidade que permite o usuário alterar um dado(livro) do banco de dados por inteiro

                # Estrutura que exibe ao usuário quais livros estão disponíveis para alteração
                print('Lista de livros cadastrados passíveis de alteração:')
                catalogo_alteracao = get()
                for livro_exibicao in catalogo_alteracao:
                    print(f"{livro_exibicao["nome"]} ({livro_exibicao["autor"]}) - {livro_exibicao["ano_de_publicacao"]}")

                # Tratamento de exceções para garantir que o usuário não preencha nenhum campo com o valor indevido
                try:
                    escolha_usuario_alteracao_de_livro = input('Nome do livro que deseja alterar: ').strip()
                    # Variável de controle que verifica se o nome do livro sugerido foi encontrado no banco de dados
                    livro_encontrado_para_alteracao = encontrar_livro(escolha_usuario_alteracao_de_livro)

                    # Caso o livro tenha sido encontrado, o processo de alteração prossegue
                    if livro_encontrado_para_alteracao:
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

                        # Função que altera um dado(livro) do banco de dados por meio de um método PUT a partir da nossa própria API
                        put(escolha_usuario_alteracao_de_livro, novo_livro_por_alteracao)
                    else:
                        # Caso o livro não tenha sido encontrado, a seguinte mensagem é emitida
                        print(f'O livro {escolha_usuario_alteracao_de_livro} não foi encontrado. Verifique se o nome foi digitado corretamente')
                except ValueError:
                    print('Por favor, digite um valor inteiro quando for inserir a data de publicação do livro')
            case '4':
                # Funcionalidade que permite o usuário excluir um dado(livro) do banco de dados

                # Estrutura que apresenta ao usuário quais livros estão passíveis de remoção
                print('Lista de livros disponíveis para remoção')
                catalogo_remocao = get()
                for livro_apresentacao in catalogo_remocao:
                    print(f"{livro_apresentacao["nome"]} ({livro_apresentacao["autor"]}) - {livro_apresentacao["ano_de_publicacao"]}")
                
                escolha_usuario_remocao_de_livro = input('Digite o livro que deseja remover: ').strip()
                # Variável de controle que verifica se o nome do livro sugerido foi encontrado no banco de dados para remoção
                livro_encontrado_para_remocao = encontrar_livro(escolha_usuario_remocao_de_livro)

                # Caso o livro tenha sido encontrado, o processo de remoção prossegue
                if livro_encontrado_para_remocao:
                    # Função que exclui um dado(livro_ do banco de dados por meio de um método DELETE a partir dad nossa própria API
                    delete(escolha_usuario_remocao_de_livro)
                else:
                    # Caso o livro não tenha sido encontrado, a seguinte mensagem é emitida
                    print(f'O livro {escolha_usuario_remocao_de_livro} não foi encontrado. Verifique se o nome foi digitado corretamente')
            case '5':
                # Estrutura que encerra a execução do programa
                print('Volte sempre :)')
                print('Encerrando o programa...')
                break
            case _:
                # Mensagem exibida caso o usuário decida não escolher uma das funcionalidades principais do programa
                print('Por favor, digite uma opção válida')


if __name__ == '__main__':
    app()

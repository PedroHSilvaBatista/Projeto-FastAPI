# Library.py

A principal ideia deste projeto é praticar e aprimorar habilidades no uso do framework FastAPI, um framework web moderno e rápido para Python, ideal para criar APIs REST, com validação automática de dados, suporte a modelos Pydantic e geração de documentação interativa.

O projeto visa simular a utilização da API criada por um usuário em um contexto de biblioteca virtual. Permite operações como:

- Visualizar os livros disponíveis armazenados.
- Adicionar um novo livro ao acervo.
- Alterar informações de um livro já registrado.
- Excluir um livro do acervo.

Este projeto aborda conceitos de:

- Programação Orientada a Objetos (POO).
- Manipulação de arquivos JSON.
- Consumo e desenvolvimento de APIs focadas no CRUD (Create, Read, Update, Delete).

---

## Funcionalidades

1. Visualizar todo o catálogo de livros (GET).  
2. Adicionar um livro ao catálogo (POST).  
3. Alterar informações de itens existentes (PUT).  
4. Remover um livro do acervo (DELETE).  
5. Sair do programa.  

---

## Tecnologias Utilizadas

- **Linguagem**: Python 3.8.10.  
- **Framework**: FastAPI.  
- **Servidor Local**: Uvicorn.  
- **Bibliotecas**: `requests`, `json`, `os`, `typing`, `pydantic`.

---

## Requisitos de Instalação

1. Certifique-se de ter o Python instalado (recomendamos a versão 3.8.10 ou superior).
2. Clone o repositório:  
   ```bash
   git clone https://github.com/usuario/nome-do-projeto.git
3. Instale as dependências:
   pip install -r requirements.txt

---

## Como usar
1. Inicie o servidor local com o seguinte comando no terminal da IDE utilizada:
   uvicorn main:app --reload
Nota: É recomendado que a execução da API seja feita em um servidor local.

2. Acesse a documentação interativa da API no navegador:

  Swagger UI: /docs
  ReDoc: /redoc

3. Faça suas requisições para os endpoints da API conforme necessário utilizando o Swagger UI.

---

## Próximos passos
 - Melhorar o Swagger UI da API para que sua utilização seja mais intuitiva.
 - Criar um arquivo JSON separado para armazenar livros reservados, diferenciando entre livros disponíveis e livros reservados.

import sqlite3

#Conectando ao banco de dados SQLite
def connect_db():
    # Conectando ao banco de dados SQLite
    # Se o arquivo não existir, ele será criado
    conexao = sqlite3.connect('titulo.db')
    return conexao

# Inserindo dados no banco de dados
def insert_data(conexao, nome, ano, nota):
    # Criando um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Inserindo dados na tabela filmes
    cursor.execute("INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)", (nome, ano, nota))

    # Salvando as alterações
    conexao.commit()
    conexao.close()

#listando os dados do banco de dados

def list_data(conexao):
    # Criando um cursor para executar comandos SQL
    cursor = conexao.cursor()

    # Lendo dados da tabela filmes
    cursor.execute("SELECT * FROM filmes")
    resultado = cursor.fetchall()

    # Fechando a conexão
    conexao.close()

    return resultado
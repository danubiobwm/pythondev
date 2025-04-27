import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conexao = sqlite3.connect('titulo.db')

# Create a cursor object to interact with the database
cursor = conexao.cursor()

# Create a table filmes
cursor.execute(
    """
      CREATE TABLE filmes (
          id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
          nome TEXT NOT NULL,
          ano INTEGER NOT NULL,
          nota REAL NOT NULL
      );
    """
)

# fechar a conexão com o banco de dados
conexao.close()
print('Tabela criada com sucesso!')
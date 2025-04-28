import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# excluir um registro
cursor.execute("DELETE FROM filmes WHERE id = 1")
conexao.commit()

# verificar se o registro foi excluído
cursor.execute("SELECT * FROM filmes")
filmes = cursor.fetchall()
for titulo in filmes:
    print(titulo)

print("Registro excluído com sucesso!")
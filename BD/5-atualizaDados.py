import sqlite3

#connect to the database
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#update data
id = 1
cursor.execute('UPDATE filmes SET nome = ? WHERE id = ?', ('O Senhor dos Anéis: A Sociedade do Anel', id))
conexao.commit()

#close the connection
conexao.close()
print("Dados atualizados com sucesso!")
import sqlite3

#connect to the database
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#insert data into the table
cursor.execute('''INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)''', ('O Senhor dos Anéis: A Sociedade do Anel', 2001, 8.8))

cursor.execute('''INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)''', ('O Senhor dos Anéis: As Duas Torres', 2002, 8.7))

cursor.execute('''INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)''', ('O Senhor dos Anéis: O Retorno do Rei', 2003, 8.9))

cursor.execute('''INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)''', ('Harry Potter e a Pedra Filosofal', 2001, 7.6))

cursor.execute('''INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)''', ('Harry Potter e a Câmara Secreta', 2002, 7.4))

cursor.execute('''INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)''', ('Harry Potter e o Prisioneiro de Azkaban', 2004, 7.8))


conexao.commit() #commit the changes to the database
conexao.close() #close the connection to the database
print('Dados inseridos com sucesso!')

import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# leitura de dados
cursor.execute('SELECT * FROM filmes')
resultado = cursor.fetchall()

for linha in resultado:
    print(linha)
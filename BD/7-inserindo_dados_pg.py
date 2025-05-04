from conexao_post import conn

cursor_obj = conn.cursor()
# Inserindo dados na tabela
games = [
    ('The Legend of Zelda: Breath of the Wild',  2017, 9.8),
    ('The Witcher 3: Wild Hunt',  2015, 8.5),
    ('Red Dead Redemption 2',  2018, 10.0),
    ('Dark Souls III',  2016, 7.6),
    ('God of War',  2018, 7.8)
    ]

for game in games:
    cursor_obj.execute('''
        INSERT INTO games (name, year, score)
        VALUES (%s, %s, %s)
    ''', game)

conn.commit()
print("Dados inseridos com sucesso!")
# Fechando a conexão
conn.close()
# O código acima insere dados na tabela "games" do banco de dados PostgreSQL.
# Ele utiliza a biblioteca psycopg2 para conectar ao banco de dados e executar comandos SQL.
# A tabela "games" deve ter sido criada previamente com os campos "title", "platform", "year" e "rating".
# O código insere uma lista de jogos com seus respectivos dados na tabela.
# Após a inserção, a conexão com o banco de dados é fechada.
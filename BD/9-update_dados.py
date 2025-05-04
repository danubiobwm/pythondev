from conexao_post import conn

cur = conn.cursor()

sql ="""
    UPDATE games
    SET NAME = %s
    WHERE ID = %s
"""

cur.execute(sql, ("The Witcher 3: Wild Hunt X", 2))
conn.commit()
print("Dados atualizados com sucesso!")
# Fechando a conexão
conn.close()


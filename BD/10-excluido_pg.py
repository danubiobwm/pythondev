import sqlite3
from conexao_post import conn


cur = conn.cursor()
sql = """
    DELETE FROM games
    WHERE ID = %s
"""
cur.execute(sql, (2,))  # Excluindo o jogo com ID 2

conn.commit()
print("Dados excluídos com sucesso!")
# Fechando a conexão
conn.close()
from conexao_post import conn

cur = conn.cursor()
cur.execute("SELECT * FROM games")
result = cur.fetchall()

for row in result:
    print(row)



cur.close()
conn.close()
import psycopg2  # type: ignore

conn = psycopg2.connect(
    host="localhost",
    database="db_games",
    user="postgres",
    password="admin",
    port="5433"
)
cur = conn.cursor()

if cur:
    print("Conexão com o banco de dados PostgreSQL realizada com sucesso.")
else:
    print("Falha na conexão com o banco de dados PostgreSQL.")
# Execute a query to check the connection
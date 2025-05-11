import pytest
import sqlite3
from usuario_sistema import adicionar_usuario, buscar_usuario

# Configuração do banco de dados para os testes
@pytest.fixture
def db_connection():
    # Cria um banco de dados em memória para os testes
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Cria a tabela de usuários
    cursor.execute("""
        CREATE TABLE usuario (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    connection.commit() # Certifique-se de commitar a criação da tabela

    yield cursor, connection

    # Fecha a conexão após os testes
    connection.close()


@pytest.mark.parametrize("id, nome, email", [
    (1, "Alice", "alice@bol.com"),
    (2, "Bob", "bob@bol.com")]
)
@pytest.mark.unit
def test_adicionar_usuario(db_connection, id, nome, email):
    cursor, connection = db_connection
    adicionar_usuario(cursor, id, nome, email)
    connection.commit()

    # Verifica se o usuário foi adicionado corretamente
    cursor.execute("SELECT * FROM usuario WHERE id = ?", (id,))
    usuario = cursor.fetchone()
    assert usuario is not None
    assert usuario[0] == id
    assert usuario[1] == nome
    assert usuario[2] == email


# Supondo que sua função buscar_usuario retorne algo que você possa testar.
def buscar_usuario(cursor, email):
    cursor.execute("SELECT * FROM usuario WHERE email = ?", (email,))
    return cursor.fetchone() # Retorna o usuário ou None se não encontrado

@pytest.mark.integration
def test_buscar_usuario_inexistente(db_connection):
    cursor, connection = db_connection
    # Testa a busca de um usuário que não existe
    usuario = buscar_usuario(cursor, "bob@g.com.br")
    # Verifica se a função retorna None quando o usuário não é encontrado
    assert usuario is None
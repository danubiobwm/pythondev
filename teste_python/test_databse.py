import pytest
import sqlite3

@pytest.fixture
def db_connection():
    # Create a temporary in-memory database
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()

    # Create a sample table
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    # Insert sample data
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 30))
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))

    # Commit the changes
    connection.commit()

    yield connection

    # Close the connection after the test
    connection.close()

def test_user_count(db_connection):
    cursor = db_connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]
    assert count == 2, f"Expected 2 users, but got {count}"
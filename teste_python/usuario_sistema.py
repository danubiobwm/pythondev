def adicionar_usuario(cursor, id, nome, email):
      """
      Adiciona um novo usuário ao banco de dados.

      Args:
          cursor: O cursor do banco de dados.
          id (int): O ID do usuário.
          nome (str): O nome do usuário.
          email (str): O email do usuário.

      Returns:
          None
      """
      # Verifica se o usuário já existe
      cursor.execute("SELECT * FROM usuario WHERE id = ?", (id,))
      if cursor.fetchone() is not None:
          print(f"Usuário com ID {id} já existe.")
          return

      # Adiciona o novo usuário
      cursor.execute("INSERT INTO usuario (id, nome, email) VALUES (?, ?, ?)", (id, nome, email))
      print(f"Usuário {nome} adicionado com sucesso.")


def buscar_usuario(cursor, email):
  cursor.execute("SELECT * FROM usuario WHERE email = ?", (email,))
  usuario = cursor.fetchone()
  if usuario:
      print(f"Usuário encontrado: ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}")
  else:
      print("Usuário não encontrado.")

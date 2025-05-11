
def is_positive(n):
  return n > 0


def sub(a, b):
  return a - b

def length(list):
  return len(list)


def validateEmail(email):
  if '@' in email and '.' in email:
    return True
  else:
    return False



def somar_lista(valores):
  """
  Somar todos os valores de uma lista.
  :param valores: lista de valores
  :return: soma dos valores
  """
  if not all(isinstance(i, (int, float)) for i in valores):
    raise ValueError("Todos os elementos da lista devem ser números.")
  return sum(valores)

def encontrar_valor(dicionario, chave):
  """
  Encontrar um valor em um dicionário.
  :param dicionario: dicionário a ser pesquisado
  :param chave: chave a ser encontrada
  :return: valor correspondente à chave ou None se não encontrado
  """
  if not isinstance(dicionario, dict):
    raise ValueError("O primeiro argumento deve ser um dicionário.")
  return dicionario.get(chave, None)
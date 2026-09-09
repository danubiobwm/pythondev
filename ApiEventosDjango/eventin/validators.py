import re
from validate_docbr import CPF


def validate_nome(nome):
  nome_limpo = nome.replace(" ", "")
  if not nome_limpo.isalpha():
    raise ("O nome só pode conter letras e espaços.")
  if len(nome.strip()) < 3:
    raise ("O nome deve ter pelo menos 3 caracteres.")
  return nome

def validate_email(email):
  if "@" not in email or "." not in email.split("@")[-1]:
    raise ("O email deve ser válido")
  return email

def validate_telefone(telefone):
  modelo = f"[0-9]{2} [0-9]{5}-[0-9]{4}"
  response = re.findall(modelo, telefone)
  return not response

def validate_cpf(numero_cpf):
  cpf = CPF()
  cpf_valido = cpf.validate(numero_cpf)
  return not cpf_valido
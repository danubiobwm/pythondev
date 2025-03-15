import re
from unittest import result

text = "Udemy - uma plataforma com muitos cursos"

# indice inicial e final de palavras
# o R signigica uma raw string strin bruta

match = re.search(r"muitos cursos", text)

print(f"Indice inicial: {match.start()}")
print(f"Indice final: {match.end()}")

# Buscando o indice que possui o ponto
site = 'https://udemy.com'
match = re.search(r"\.", site)
print(match)

# Buscado uma lista de caracteres dentro de uma frase

pattern = "[g-m]"
result = re.findall(pattern, text)
print(result)

# Verificando o inicio de uma string
rule = r'^A'
phrases = ['A casa está suja', 'o dia está lindo', 'Vamos passe']
for f in phrases:
  if re.match(rule, f):
    print(f"Corresponde:{f}")
  else:
    print(f" Não Corresponde:{f}")

# vereficando o final de uma string
rule_end = r'!$'
phrase2 = "O dia está linda!"
match = re.search(rule_end, phrase2)

if match:
  print("Sim, corresponde")
else:
  print("Não, corresponde")
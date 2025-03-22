class Biblioteca:
  biblioteca = []

  def __init__(self, nome):
    self.nome = nome
    self._ativo = False
    Biblioteca.biblioteca.append(self)

  def __str__(self):
    return self.nome

  @classmethod
  def listar_bibliotecas(cls):
    print(f"{'Bibliotecas cadastradas'.ljust(25)} | {'Status'}")
    for biblioteca in Biblioteca.biblioteca:
      print(f"{biblioteca.nome.ljust(25)} |  {biblioteca.ativo}")

  def alterna_estado():
    self._ativo = not self._ativo

  @property
  def ativo(self):
    "ativada" if self._ativo else "desativada"


biblioteca_cidade = Biblioteca("Biblioteca da cidaded")
biblioteca_shopping = Biblioteca("Biblioteca do shopping")

print(biblioteca_cidade)
print(biblioteca_shopping)

Biblioteca.listar_bibliotecas()


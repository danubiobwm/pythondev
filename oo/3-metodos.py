class Game:
  def __init__(self, name, yearLaunch, multiplayer, note):
    self.name = name
    self.yearLaunch = yearLaunch
    self.multiplayer = multiplayer
    self.note = note

  def __str__(self):
      return "Nome:{} Ano de lançamento:{} Multiplayer:{} Nota:{}".format(self.name, self.yearLaunch, self.multiplayer, self.note)

print("Criando objeto game1")
game1 = Game("Super Mario", 1985, False, 10)
print(game1)
print("Criando objeto game2")
game2 = Game("Counter Strike", 2000, True, 9.5)
print(game2)


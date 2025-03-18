class Game:
  name = ""
  yearLaunch = 0
  multiplayer = False
  note=0

#Primeiro game
game1 = Game()
game1.name = "Super Mario"
game1.yearLaunch = 1985
game1.multiplayer = False
game1.note = 10

#Segundo game
game2 = Game()
game2.name = "Super Mario 64"
game2.yearLaunch = 1996
game2.multiplayer = False
game2.note = 10


print("Nome:{} Ano de lançamento:{} Multiplayer:{} Nota:{}".format(game1.name, game1.yearLaunch, game1.multiplayer, game1.note))
print("Nome:{} Ano de lançamento:{} Multiplayer:{} Nota:{}".format(game2.name, game2.yearLaunch, game2.multiplayer, game2.note))

class Game:
  total_games = 0 # Variavel de Classe para contar o total de jogos criados
  def __init__(self, name, yearLaunch, multiplayer, note):
    self.name = name
    self.yearLaunch = yearLaunch
    self.multiplayer = multiplayer
    self.note = note
    Game.total_games += 1
    self.totalEvaluation = 0
    self.evaluatiors = 0

  def __str__(self):
      return "Nome:{} Ano de lançamento:{} Multiplayer:{} Nota:{}".format(self.name, self.yearLaunch, self.multiplayer, self.note)

  def technical_sheet(self):
    print(f"Nome: {self.name}" )
    print(f"Ano de lançamento: {self.yearLaunch}")
    print(f"Multiplayer: {self.multiplayer}" )
    print(f"Nota: {self.note}\n")


class GameStudio:
  def __init__(self, name=""):
    self.name = name
    self.games = []

  def add_game(self, game):
    self.games.append(game)

  def evaluate_studio_quality(self):
    total_notes = sum(game.note for game in self.games)
    num_games = len(self.games)
    if num_games == 0:
      print(f"o studio {self.name} não tem jogos")
    else:
      print(f"A média das notas dos jogos do studio {self.name} é {total_notes/num_games}")


game1 = Game("The Witcher 3", 2015, True, 10)

game2 = Game("GTA V", 2013, True, 9.5)

game3 = Game("Cyberpunk 2077", 2020, True, 8)

studio = GameStudio("CD Projekt Red")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)
studio.evaluate_studio_quality()

for game in studio.games:
  game.technical_sheet()
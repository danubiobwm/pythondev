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

  def aveluate(self, note):
    self.totalEvaluation += note
    self.evaluatiors += 1
    self.note = note

  def average(self):
    if self.evaluatiors > 0:
      print(f"Media do jogo {self.name}: {self.totalEvaluation / self.evaluatiors}")
    else:
      print(f"O jogo {self.name} ainda não possui avaliações.")

#class devivada de Game - especializada

class SinglePlayerGame(Game):
  def __init__(self, name="", yearLaunch=0, note=0, storyLine=""):
    super().__init__(name, yearLaunch, False, note)
    self.storyLine = storyLine

  def technical_sheet(self):
    super().technical_sheet()
    print(f"História: {self.storyLine}\n")

mult_game = Game("GTA V", 2013, True, 10)
mult_game.technical_sheet()
mult_game.aveluate(9)
mult_game.average()

single_game = SinglePlayerGame("The Last of Us", 2013, 10, "Joel e Ellie")
single_game.technical_sheet()
single_game.aveluate(10)
single_game.average()








class Game:
  def __init__(self, name, yearLaunch, multiplayer, note):
    self.name = name
    self.yearLaunch = yearLaunch
    self.multiplayer = multiplayer
    self.totalEvaluation = 0
    self.evaluatiors = 0
    self.note = note

  def __str__(self):
      return "Nome:{} Ano de lançamento:{} Multiplayer:{} Nota:{}".format(self.name, self.yearLaunch, self.multiplayer, self.note)

  def technical_sheet(self):
    print("Criando objeto game1")
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

game1 = Game("The Witcher 3", 2015, True, 10)
game1.technical_sheet()
game1.aveluate(7)
game1.aveluate(10)
game1.average()

game2 = Game("GTA V", 2013, True, 9.5)
game2.technical_sheet()
game2.aveluate(9)
game2.aveluate(8)
game2.average()




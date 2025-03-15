import os

#return a pasta atual
print(os.getcwd())
# Listar arquivos e pastas
print(os.listdir())
#versao do sistema
os.system("ver")
#conf da maquinas
os.system("systeminfo")
# limpa a tela do terminal
os.system("cls")
# Desliga o computador
# os.system("shutdown /s")
# os.system("shutdown /s /t 0")
os.system("shutdown /a")


def turn_off_one_hours():
  os.system("shutdown /s /t 3600")

def turn_off_half_an_hour():
  os.system("shutdown /s /t 1800")

def cancel_shutdown():
  os.system("shutdown /a")


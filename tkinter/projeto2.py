from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from random import *
from paises import *

# Cores
co0 = "#444466" # Preta
co1 = "#feffff" # branca
co2 = "#6f9fbd" # azul
co3 = "#38576b"
co4 = "#403d3d"
fundo_cima = "#2aa6a8"

fundo = co1
cor1 = "#f0ba4f"

janela = Tk()
janela.title("Qual país")
janela.geometry("350x310")
janela.configure(bg=co1)

# Frames
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=172)
frame_cima = Frame(janela, width=350, height=60, bg=fundo_cima,
                   pady=0, padx=0, relief="flat")

frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=350, height=300, bg=fundo,
                   pady=12, padx=0, relief="flat")

frame_baixo.grid(row=2, column=0, sticky=NW)
style = ttk.Style(janela)
style.theme_use("default")
style.configure("black.Horizontal.TProgressBar", background="#fcc058")
style.configure("TProgressbar", thickness=5)

global pontos, vida, nome_do_pais, img_bandeira
pontos = 0
vida = 3

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=172)

frame_cima = Frame(janela, width=350, height=60, bg=fundo_cima,
                   pady=0, padx=0, relief="flat")
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=350, height=300, bg=fundo,
                   pady=12, padx=0, relief="flat")
frame_baixo.grid(row=2, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use("default")
style.configure("black.Horizontal.TProgressBar", background="#fcc058")
style.configure("TProgressBar", thickness=5)


app_nome  = Label(frame_cima, text="QUAL O PAÍS?", relief="flat",
                  anchor="center", font=("Fixedsys 20"), bg=fundo_cima, fg=co1)
app_nome.place(x=15, y=15)

bar = Progressbar(frame_baixo, length=293, style="black.Horizontal.TProgressbar")
bar.place(x=27, y=50)
bar['value'] = pontos

l_score = Label(frame_baixo, text="Pontuação: "+str(pontos),
                font=("System 17"), bg=fundo, fg=co0)
l_score.place(x=27, y=10)

janela.mainloop()
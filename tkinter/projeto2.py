from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
from random import *
from paises import *

# Cores
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#6f9fbd"  # azul
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
frame_cima = Frame(
    janela, width=350, height=60, bg=fundo_cima, pady=0, padx=0, relief="flat"
)

frame_cima.grid(row=1, column=0)

frame_baixo = Frame(
    janela, width=350, height=300, bg=fundo, pady=12, padx=0, relief="flat"
)

frame_baixo.grid(row=2, column=0, sticky=NW)
style = ttk.Style(janela)
style.theme_use("default")
style.configure("black.Horizontal.TProgressBar", background="#fcc058")
style.configure("TProgressbar", thickness=5)

global pontos, vida, nome_do_pais, img_bandeira
pontos = 0
vida = 3

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=172)

frame_cima = Frame(
    janela, width=350, height=60, bg=fundo_cima, pady=0, padx=0, relief="flat"
)
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(
    janela, width=350, height=300, bg=fundo, pady=12, padx=0, relief="flat"
)
frame_baixo.grid(row=2, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use("default")
style.configure("black.Horizontal.TProgressBar", background="#fcc058")
style.configure("TProgressBar", thickness=5)


app_nome = Label(
    frame_cima,
    text="QUAL O PAÍS?",
    relief="flat",
    anchor="center",
    font=("Fixedsys 20"),
    bg=fundo_cima,
    fg=co1,
)
app_nome.place(x=15, y=15)

bar = Progressbar(frame_baixo, length=293, style="black.Horizontal.TProgressbar")
bar.place(x=27, y=50)
bar["value"] = pontos

l_score = Label(
    frame_baixo, text="Pontuação: " + str(pontos), font=("System 17"), bg=fundo, fg=co0
)
l_score.place(x=27, y=10)

# imagens
img_0 = Image.open("0.png")
img_0 = img_0.resize((30, 30))
img_0 = ImageTk.PhotoImage(img_0)

img_1 = Image.open("1.png")
img_1 = img_1.resize((30, 30))
img_1 = ImageTk.PhotoImage(img_1)

l_icon_1 = Label(frame_baixo, image=img_1, bg=fundo)
l_icon_1.place(x=290, y=10)

l_icon_2 = Label(frame_baixo, image=img_1, bg=fundo)
l_icon_2.place(x=259, y=10)

l_icon_3 = Label(frame_baixo, image=img_1, bg=fundo)
l_icon_3.place(x=228, y=10)

l_pergunta = Label(
    frame_baixo,
    text="Qual pais pertence essa bandeira?",
    pady=0,
    padx=0,
    relief="flat",
    anchor="center",
    font=("Ivy 10"),
    bg=fundo,
    fg=co4,
)

l_pergunta.place(x=30, y=70)
# campo para resposta
e_resposta = Entry(
    frame_baixo,
    width=15,
    justify="center",
    font=("", 12),
    highlightthickness=1,
    relief="solid",
)
e_resposta.place(x=178, y=100)


def inicia_jogo():
    global pontos, vida, nome_do_pais, img_bandeira, l_icon_bandeira
    dados = dados_pais()
    nome_do_pais = dados[1]
    imagem = dados[0]

    # image bandeira
    img_bandeira = Image.open(imagem)
    img_bandeira = img_bandeira.resize((140, 100))
    img_bandeira = ImageTk.PhotoImage(img_bandeira)

    l_icon_bandeira = Label(frame_baixo, image=img_bandeira, bg=fundo, relief="solid")
    l_icon_bandeira.place(x=30, y=100)


def reiniciar_jogo():
    global pontos, nome_do_pais, vida, img_0, img_1
    pontos = 0
    vida = 3
    bar["value"] = pontos
    l_score["text"] = "Pontuação: " + str(pontos)
    l_icon_1["image"] = img_1
    l_icon_2["image"] = img_1
    l_icon_3["image"] = img_1

    inicia_jogo()


def game_over():
    global pontos, nome_do_pais, vida, img_0, img_1
    pontos = 0
    vida = 3
    bar["value"] = pontos
    l_score["text"] = "Pontuação: " + str(pontos)
    l_icon_1["image"] = img_1
    l_icon_2["image"] = img_1
    l_icon_3["image"] = img_1

    inicia_jogo()


def verificar():
    global pontos, vida
    resposta = e_resposta.get()
    if resposta == nome_do_pais:
        pontos += 10
        l_score["text"] = "Pontuação: " + str(pontos)
        bar["value"] = pontos
        l_icon_1["image"] = img_0
        l_icon_2["image"] = img_1
        l_icon_3["image"] = img_1
        inicia_jogo()
    else:
        vida -= 1
        if vida == 2:
            l_icon_1["image"] = img_0
            messagebox.showinfo("Resposta errada", "Você ainda tem mais 2 vidas")
            e_resposta.delete(0, END)
            inicia_jogo()
        elif vida == 1:
            l_icon_2["image"] = img_0
            messagebox.showinfo("Resposta errada", "Você ainda tem mais 1 vida")
            e_resposta.delete(0, END)
            inicia_jogo()
        elif vida == 0:
            l_icon_3["image"] = img_0
            messagebox.showinfo("Game Over", "Você perdeu todas as vidas")
            reiniciar_jogo()

    if bar["value"] == 100:
        messagebox.showinfo("Parabéns", "Você ganhou o jogo")
        reiniciar_jogo()
    else:
        inicia_jogo()


b_resposta = Button(
    frame_baixo,
    text="Confirmar",
    width=10,
    height=1,
    bg=co1,
    fg=co4,
    font=("Ivy 8 bold"),
    relief=RAISED,
    overrelief=RIDGE,
    command=verificar,
)
b_resposta.place(x=210, y=150)


inicia_jogo()

janela.mainloop()

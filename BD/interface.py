import tkinter as tk
import orm
from tkinter import messagebox


#funcao para adicionar um filme
def add_movie():
    try:
        nome = entry_nome.get()
        ano = entry_ano.get()
        nota = entry_nota.get()

        if not id or not nome or not ano or not nota:
            raise ValueError("Todos os campos devem ser preenchidos.")

        # Adiciona o filme ao banco de dados
        orm.adicionar_filme(nome, ano, nota)
        messagebox.showinfo("Sucesso", "Filme adicionado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


#funcao para atualizar um filme
def update_movie():
    try:
        id = entry_id.get()
        name = entry_nome.get()
        ano = entry_ano.get()
        nota = entry_nota.get()

        if not id or not name or not ano or not nota:
            raise ValueError("Todos os campos devem ser preenchidos.")

        # Atualiza o filme no banco de dados
        orm.atualizar_filme(id, name, ano, nota)
        messagebox.showinfo("Sucesso", "Filme atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


#funcao para deletar um filme
def delete_movie():
    try:
        id = entry_id.get()

        if not id:
            raise ValueError("O campo ID deve ser preenchido.")

        # Deleta o filme do banco de dados
        orm.deletar_filme(id)
        messagebox.showinfo("Sucesso", "Filme deletado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# interface Grafica
root = tk.Tk()
root.title("Gerenciador de Tarefas")

# Rotulos e campos de entrada
label_id = tk.Label(root, text="ID:")
label_id.grid(row=0, column=0)
entry_id = tk.Entry(root, width=50)
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(root, text="Nome:")
label_nome.grid(row=1, column=0)
entry_nome = tk.Entry(root, width=50)
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_ano = tk.Label(root, text="Ano:")
label_ano.grid(row=2, column=0)
entry_ano = tk.Entry(root, width=50)
entry_ano.grid(row=2, column=1, padx=10, pady=5)

label_nota = tk.Label(root, text="Nota:")
label_nota.grid(row=3, column=0)
entry_nota = tk.Entry(root, width=50)
entry_nota.grid(row=3, column=1, padx=10, pady=5)

button_adicionar = tk.Button(root, text="Adicionar Filme", command=add_movie)
button_adicionar.grid(row=4, column=0, columnspan=2, pady=5)

button_atualizar = tk.Button(root, text="Atualizar Filme", command=update_movie)
button_atualizar.grid(row=5, column=0, columnspan=2, pady=5)

button_excluir = tk.Button(root, text="Excluir Filme", command=delete_movie)
button_excluir.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()

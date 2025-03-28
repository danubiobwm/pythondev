from  modelos.biblioteca import Biblioteca
from modelos.itens.livro import Livro
from modelos.itens.revista import Revista


biblioteca_cidade = Biblioteca("Biblioteca da Cidade")
biblioteca_shopping = Biblioteca("Biblioteca do Shopping")

livro1 = Livro("Dom Casmurro", "Machado de Assis", 199, 200)
livro2 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 100)
revista1 = Revista("Super Interessante", "Abril", 87, 1)
revista2 = Revista("Super Interessante", "Abril", 87, 2)

livro1.aplicar_desconto(10)

biblioteca_cidade.adicionar_item(livro1)
biblioteca_cidade.adicionar_item(livro2)
biblioteca_cidade.adicionar_item(revista1)
biblioteca_cidade.adicionar_item(revista2)

biblioteca_shopping.adicionar_item(livro1)
biblioteca_shopping.adicionar_item(livro2)
biblioteca_shopping.adicionar_item(revista1)
biblioteca_shopping.adicionar_item(revista2)



def main():
  Biblioteca.listar_bibliotecas()
  biblioteca_cidade.exibir_itens()



if __name__ == "__main__":
  main()
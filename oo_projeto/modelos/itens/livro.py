from modelos.itens.item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, isbn):
        super().__init__(titulo, autor, preco)
        self.isbn = isbn

    def aplicar_desconto(self, percentual):
        # Aplica desconto apenas no preço do livro
        self._preco -= self._preco * percentual / 100
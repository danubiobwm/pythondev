from modelos.itens.item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, titulo, autor, preco, edicao):
        super().__init__(titulo, autor, preco)
        self.edicao = edicao

    def aplicar_desconto(self, percentual):
        # Aplica desconto apenas no preço da revista
        self._preco -= self._preco * percentual / 100
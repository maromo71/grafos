class Produto:
    def __init__(self, cod, nome, preco):
        self.cod = cod
        self.nome = nome
        self.preco = preco
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco <0:
            raise ValueError("Preco dever positivo")
        self.__preco = novo_preco


produto1 = Produto(122, "Camisa Nike", 125.89)
print(produto1.nome)
print(produto1.cod)
print(produto1.preco)

class Categoria:
    def __init__(self, descricao):
        self.__descricao = descricao

c1 = Categoria("Alimento e Bebida")
c2 = Categoria("Automotivo")        
c3 = Categoria("Bebê")

class Produto:
    def __init__(self, descricao, preco, estoque, categoria):
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__categoria = categoria

p1 = Produto("Café 3 Corações", 10, 100, c1)
p2 = Produto("Coca-cola", 5, 50, c1)
p3 = Produto("Fralda", 20, 30, c3)


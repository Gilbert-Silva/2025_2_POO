class Categoria:
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao

c1 = Categoria(1, "Alimento e Bebida")
c2 = Categoria(2, "Automotivo")        
c3 = Categoria(3, "Bebê")

class Produto:
    def __init__(self, id, descricao, preco, estoque, id_categoria):
        self.__id = id
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque
        self.__id_categoria = id_categoria

p1 = Produto(1, "Café 3 Corações", 10, 100, 1)
p2 = Produto(2, "Coca-cola", 5, 50, 1)
p3 = Produto(3, "Fralda", 20, 30, 3)



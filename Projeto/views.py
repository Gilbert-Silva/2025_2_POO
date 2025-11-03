from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO

class View:
    def cliente_inserir(nome):
        id = 0
        c = Cliente(id, nome)
        ClienteDAO.inserir(c)
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_atualizar(id, nome):
        c = Cliente(id, nome)
        ClienteDAO.atualizar(c)
    def cliente_excluir(id):
        nome = ""
        c = Cliente(id, nome)
        ClienteDAO.excluir(c)

    def categoria_inserir(descricao):
        id = 0
        c = Categoria(id, descricao)
        CategoriaDAO.inserir(c)
    def categoria_listar():
        return CategoriaDAO.listar()
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)
    def categoria_excluir(id):
        descricao = ""
        c = Categoria(id, descricao)
        CategoriaDAO.excluir(c)

    


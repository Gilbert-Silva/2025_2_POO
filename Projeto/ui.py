#from models.cliente import Cliente, ClienteDAO
#from models.categoria import Categoria, CategoriaDAO
from views import View

class UI: # classe estática -> não tem instância     
    def menu():
        print("Clientes")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print()
        print("Categorias")
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print()
        print("9 - Fim")
        return int(input("Informe uma opção: "))           
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()

    def cliente_inserir():
        #id = int(input("Informe o id: "))
        #id = 0
        nome = input("Informe o nome: ")
        #c = Cliente(id, nome)
        #ClienteDAO.inserir(c)
        View.cliente_inserir(nome)

    def cliente_listar():
        #for obj in ClienteDAO.listar(): print(obj)       
        for obj in View.cliente_listar(): print(obj)       

    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        #c = Cliente(id, nome)
        #ClienteDAO.atualizar(c)
        View.cliente_atualizar(id, nome)

    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        #nome = ""
        #c = Cliente(id, nome)
        #ClienteDAO.excluir(c)
        View.cliente_excluir(id)

    def categoria_inserir():
        #id = 0
        descricao = input("Informe a descrição: ")
        #c = Categoria(id, descricao)
        #CategoriaDAO.inserir(c)
        View.categoria_inserir(descricao)
    def categoria_listar():
        #for obj in CategoriaDAO.listar(): print(obj) 
        for obj in View.categoria_listar(): print(obj)      
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        #c = Categoria(id, descricao)
        #CategoriaDAO.atualizar(c)
        View.categoria_atualizar(id, descricao)
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        #descricao = ""
        #c = Categoria(id, descricao)
        #CategoriaDAO.excluir(c)
        View.categoria_excluir(id)

UI.main()

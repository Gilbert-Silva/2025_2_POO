import json
class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

class ClienteDAO:
    def __init__(self):
        self.objetos = []
    def inserir(self, cliente):
        self.objetos.append(cliente)
    def listar(self):
        return self.clientes
    def atualizar(self, cliente):
        for obj in self.objetos:
            if obj.id == cliente.id:
                obj.nome = cliente.nome
    def excluir(self, cliente):
        for obj in self.objetos:
            if obj.id == cliente.id:
                self.objetos.remove(obj)

class UI:     
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Fim")
        return int(input("Informe uma opção: "))           
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
    def inserir():
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        c = Cliente(id, nome)
        dao = ClienteDAO() # instanciar DAO vai criar várias listas de clientes
        dao.inserir(c)        
    def listar():
        pass        
    def atualizar():
        pass        
    def excluir():
        pass        

UI.main()


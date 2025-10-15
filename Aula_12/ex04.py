import json
class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

class ClienteDAO:
    objetos = []
    @classmethod
    def inserir(cls, cliente):
        cls.objetos.append(cliente)
    @classmethod
    def listar(cls):
        return cls.clientes
    @classmethod
    def atualizar(cls, cliente):
        for obj in cls.objetos:
            if obj.id == cliente.id:
                obj.nome = cliente.nome
    @classmethod
    def excluir(cls, cliente):
        for obj in cls.objetos:
            if obj.id == cliente.id:
                cls.objetos.remove(obj)

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
        ClienteDAO().inserir(c)
    def listar():
        pass        
    def atualizar():
        pass        
    def excluir():
        pass        

UI.main()


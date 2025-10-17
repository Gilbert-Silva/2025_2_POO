import json
class Cliente:
    def __init__(self, id, nome):
        self.id = id          # atributo de instância
        self.nome = nome      # cada cliente (instância) tem id e nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

class ClienteDAO:             # classe estática -> não tem instância
    objetos = []              # atributo da classe
    @classmethod              # classe DAO não vai ter instância
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1    
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            #aux.nome = obj.nome
            # remove o objeto antigo aux e insere o novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Cliente(dic["id"], dic["nome"])
                    cls.objetos.append(c)
        except:
            pass            


class UI: # classe estática -> não tem instância     
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
        #id = int(input("Informe o id: "))
        id = 0
        nome = input("Informe o nome: ")
        c = Cliente(id, nome)
        ClienteDAO.inserir(c)
    def listar():
        for obj in ClienteDAO.listar():
            print(obj)       
    def atualizar():
        UI.listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        c = Cliente(id, nome)
        ClienteDAO.atualizar(c)
    def excluir():
        UI.listar()
        id = int(input("Informe o id a ser excluído: "))
        nome = ""
        c = Cliente(id, nome)
        ClienteDAO.excluir(c)

UI.main()


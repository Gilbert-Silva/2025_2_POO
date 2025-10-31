import json
from datetime import datetime

class Pessoa:
    def __init__(self, id, nome, nascimento):
        self.set_id(id)
        self.set_nome(nome)
        self.set_nascimento(nascimento)
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido")
        self.__nome = nome
    def set_nascimento(self, nascimento):
        if nascimento >= datetime.now(): raise ValueError("Data inválida")
        self.__nascimento = nascimento
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_nascimento(self): return self.__nascimento
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__nascimento.strftime("%d/%m/%Y")}" 
    def to_json(self):
        return { "id" : self.__id, "nome" : self.__nome, \
            "nascimento" : self.__nascimento.strftime("%d/%m/%Y") }
    @staticmethod
    def from_json(dic):
        return Pessoa(dic["id"], dic["nome"], \
            datetime.strptime(dic["nascimento"], "%d/%m/%Y"))
    

class PessoaDAO:              # classe estática -> não tem instância
    objetos = []              # atributo da classe
    @classmethod              # classe DAO não vai ter instância
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.get_id() > id: id = aux.get_id()
        obj.set_id(id + 1)    
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
            if obj.get_id() == id: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            #aux.nome = obj.nome
            # remove o objeto antigo aux e insere o novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.get_id())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("pessoas.json", mode="w") as arquivo:
            #json.dump(cls.objetos, arquivo, default = vars, indent=4)
            json.dump(cls.objetos, arquivo, default = Pessoa.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("pessoas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    #c = Categoria(dic["id"], dic["descricao"])
                    c = Pessoa.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            


import json
from datetime import datetime, timedelta

class Corrida:
    def __init__(self, id, id_pessoa, data, distancia, tempo):
        self.set_id(id)
        self.set_id_pessoa(id_pessoa)
        self.set_data(data)
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    def set_id(self, id):
        self.__id = id
    def set_id_pessoa(self, id_pessoa):
        self.__id_pessoa = id_pessoa
    def set_data(self, data):
        if data >= datetime.now(): raise ValueError("Data inválida")
        self.__data = data
    def set_distancia(self, distancia):
        if distancia < 0: raise ValueError("Distância inválida")
        self.__distancia = distancia
    def set_tempo(self, tempo):
        if tempo < timedelta(): raise ValueError("Tempo inválido")
        self.__tempo = tempo

    def get_id(self): return self.__id
    def get_id_pessoa(self): return self.__id_pessoa
    def get_data(self): return self.__data
    def get_distancia(self): return self.__distancia
    def get_tempo(self): return self.__tempo

    def pace(self):
        return (self.__tempo.seconds/60)/(self.__distancia/1000)

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime("%d/%m/%Y")} - distância: {self.__distancia}m - tempo: {self.__tempo} - pace: {self.pace():.2f}" 
    def to_json(self):
        return { "id" : self.__id, "id_pessoa" : self.__id_pessoa, \
            "data" : self.__data.strftime("%d/%m/%Y"), \
            "distancia" : self.__distancia, \
            "tempo" : self.__tempo.seconds }
    @staticmethod
    def from_json(dic):
        return Corrida(dic["id"], dic["id_pessoa"], \
            datetime.strptime(dic["data"], "%d/%m/%Y"), \
            dic["distancia"], timedelta(seconds=dic["tempo"]))

class CorridaDAO:             # classe estática -> não tem instância
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
        with open("corridas.json", mode="w") as arquivo:
            #json.dump(cls.objetos, arquivo, default = vars, indent=4)
            json.dump(cls.objetos, arquivo, default = Corrida.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("corridas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    #c = Categoria(dic["id"], dic["descricao"])
                    c = Corrida.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            


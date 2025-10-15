import json
class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"

clientes = []

with open("clientes.json", mode="r") as arquivo:
    list_dic = json.load(arquivo)
    for dic in list_dic:
        c = Cliente(dic["id"], dic["nome"])
        clientes.append(c)

for c in clientes: print(c)

#streamlit

CRUD
C - Create
R - Read
U - Update
D - Delete
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"{self.nome} - {self.idade}"
    def __lt__(self, other):
        return self.idade < other.idade

a = Aluno("Raquel", 20)
b = Aluno("Miguel", 18)
c = Aluno("Sarah", 21)
d = Aluno("Gustavo", 19)

lista = [a, b, c, d]

for obj in lista:
    print(obj)

# Python não tem a implementação do < usado na comparação
# print(min(lista))

# Solução 1
m = lista[0]
for obj in lista:
    if obj.idade < m.idade: m = obj
print(m)

# Solução 2
def comparar_aluno(a): return a.idade
#lambda a : a.idade
print(min(lista, key = comparar_aluno))

# Solução 3
print(min(lista, key = lambda a : a.idade))

x = lambda a : a.idade
print(type(x))
print(x(d))
y = print
y("Olá")
y(x(d))

# Solução 4
print(min(lista))
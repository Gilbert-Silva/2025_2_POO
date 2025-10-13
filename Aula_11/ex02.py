class Aluno:
    def __init__(self, nome, matricula, idade):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade

a = Aluno("Raquel", "20251014040000", 19)
b = Aluno("Miguel", "20251014040001", 18)

print(a.__dict__)
print(vars(b))

x = vars(b)
for item in x.items():
    print(item, type(item))
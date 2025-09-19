# referência
# A variável é uma referência para uma instância do tipo
x = 5
y = 5

s = "POO"
# "POO" é uma instância da classe string
# s é uma variável. Ela guarda um endereço. Nesse endereço tem o texto.
x = "POO"

print(id(x))
print(id(y))



class Triangulo:
    pass

a = Triangulo()
print(a)

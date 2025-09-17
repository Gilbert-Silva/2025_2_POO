# Entidade
class Triangulo:  # não usar print ou input
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2

# Interface com o usuário
x = Triangulo()
x.b = float(input("Informe a base do triângulo: "))
x.h = float(input("Informe a altura: "))
print("Área = ", x.calc_area())

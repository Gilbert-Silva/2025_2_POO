# Entidade
class Triangulo:  # não usar print ou input
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()
x.b = 10
x.h = 20
y = x

#y = Triangulo()
y.b = 30
y.h = 40
print(x.b, x.h)

x = 10
y = 20

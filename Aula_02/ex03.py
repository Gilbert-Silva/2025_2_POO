class Triangulo:
    def __init__(self):
        self.b = 0                   # atributo ou campo
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2   # método 

x = Triangulo()
t = Triangulo()
print(x.b, x.h)
print(t.b, t.h)        
x.b = 10
x.h = 20
t.b = 30
t.h = 40
print(x.b, x.h)
print(t.b, t.h)
#print(x.b * x.h / 2)
#print(t.b * t.h / 2)
print(x.calc_area())
print(t.calc_area())



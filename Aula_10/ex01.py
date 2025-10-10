from math import sqrt
print(sqrt(16))

#import datetime
#datetime.datetime

from datetime import datetime, date, time

x = datetime(2025, 10, 10)
y = datetime(2025, 10, 10, 10, 30)
print(x)
print(y)

d = date(2025, 10, 10)
t = time(10, 30)
print(d)
print(t)

a = datetime.today()
b = datetime.now()
print(a)
print(b)

c = datetime.strptime("23/06/2023 09:30", "%d/%m/%Y %H:%M")

print(c.day)
print(c.month)
print(c.year)


i = int(input("Informe um valor inteiro: "))
print(i)

#d = datetime(input("Informe uma data: "))
# strptime - converte uma string em um datetime
# é um método de classe, ou seja, chamado com a classe

d = datetime.strptime(input("Informe uma data: "), "%d/%m/%Y")
print(d)

# propriedades - semelhantes à atributos, chamados com a instância
print(d.day)
print(d.month)
print(d.year)

# métodos de instância, chamados com a instância
print(d.date())
print(d.time())
print(d.weekday())
print(d.strftime("%d/%m/%Y"))




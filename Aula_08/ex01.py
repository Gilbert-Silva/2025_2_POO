x = []
y = list()
z = x
print(id(x), type(x))
print(id(y), type(y))
print(id(z), type(z))
x.append(10)
y.append(20)
z.append(30)
print(z[0])
print(z[1])
z = [1, 2, 3, "Teste"]
x = z
print(max(z))


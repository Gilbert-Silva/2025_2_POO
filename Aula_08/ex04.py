x = [4, 2, 1, 3]
y = x
z = x[:]
print(id(x), id(y), id(z))

print(len(x)) # x.len()
x.append(5)
x.insert(0, 10)
print(x)

x.insert(len(x), 15)
print(x)
print(x.index(1))
print(sorted(x, reverse=True))
print(x.sort())
print(x)

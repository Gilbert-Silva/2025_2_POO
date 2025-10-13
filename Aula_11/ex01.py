x = []
y = ()
z = {}

print(type(x), type(y), type(z))

y = (1, 5, 8)
print(y[0])
x = [1, 5, 8]
z = { "RN": "Natal" , "PB": "João Pessoa" , "PE": "Recife", 1 : "Teste" }
print(z["RN"])
print(z[1])
print(z)
z[2] = "POO"
z[3] = ["TADS", "Redes"]
print(z)
z[4] = z
z[5] = x
print(z)



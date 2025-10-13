x = { 2 : "POO", 10 : "Redes"}
print(max(x))

y = { "a" : "POO", "B" : "Redes"} # Lexicográfica
print(max(y))

z = ["álan", "andré"]#, 1]
z.sort()
print(z)

z = ["álan", "andré"]
z_ordenado = sorted(z, key=str.lower)
print(z_ordenado)


s = input("Informe um texto: ")
for c in s:
    s = s[1:] + s[0]
    print(s)

    
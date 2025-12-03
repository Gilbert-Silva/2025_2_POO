ok = False
while not ok:
    try:
        n = int(input("Informe um inteiro: "))
        print(2*n)
        ok = True
    except:
        print("Valor não é um inteiro")

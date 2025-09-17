data = input("Digite uma data no formato dd/mm/aaaa: ")
d, m, a = map(int, data.split("/"))  #split: "17/09/2025" -> ["17", "09", "2025"]

#lista = data.split("/")  # split: "17/09/2025" -> ["17", "09", "2025"]
#d = int(lista[0])
#m = int(lista[1])
#a = int(lista[2])

max = 31
if m in [4, 6, 9, 11]: 
    max = 30
if m == 2:
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0): max = 29
    else: max = 28
if 1 <= d <= max and 1 <= m <= 12: print("Data válida")
else: print("Data inválida")



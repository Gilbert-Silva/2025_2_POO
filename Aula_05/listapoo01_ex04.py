class Ingresso:            # entidade - tem instâncias
    def __init__(self):
        self.dia = "dom"   # definição dos atributos
        self.hora = 17
    def inteira(self):
        if self.dia == "qua": return 8
        if self.dia in ["seg", "ter", "qui"]: valor = 16
        else: valor = 20
        if self.hora == 0 or self.hora >= 17: valor *= 1.5
        return valor    

class UI:       # interface com o usuário -  não tem instância
    @staticmethod
    def main(): # método estático é um método chamado com a classe 
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.ingresso()
            if op == 2: UI.viagem()
    @staticmethod
    def menu():
        print("1-Ingresso, 2-Viagem, 3-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def ingresso():
        x = Ingresso()  # Ingresso.__init__()
        x.dia = input("Informe o dia [dom, seg, ... sab]: ")
        x.hora = int(input("Informe a hora [0-23]: "))
        print(x.dia)
        print(x.hora)
        print(f"Valor do ingresso R$ {x.inteira():.2f}")
    @staticmethod
    def viagem():
        pass

UI.main()

"""
op = 0
while op != 2:
    print("1-Ingresso, 2-Fim")
    op = int(input("Escolha uma opção: "))
    if op == 1: 
        x = Ingresso()  # Ingresso.__init__()
        x.dia = input("Informe o dia [dom, seg, ... sab]: ")
        x.hora = int(input("Informe a hora [0-23]: "))
        print(x.dia)
        print(x.hora)
"""

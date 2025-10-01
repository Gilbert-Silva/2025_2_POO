#import ingresso
from ingresso import Ingresso

class UI:       # interface com o usuário -  não tem instância
    @staticmethod
    def main(): # método estático é um método chamado com a classe 
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.ingresso()  # ingresso é chamado com a classe UI
            if op == 2: UI.viagem()
    @staticmethod
    def menu():
        print("1-Ingresso, 2-Viagem, 3-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def ingresso():
        try:
            d = input("Informe o dia [dom, seg, ... sab]: ")
            h = int(input("Informe a hora [0-23]: "))
            x = Ingresso(d, h)   # Ingresso.__init__()
            print(x)             # Ingresso.__str__()
            print(x.get_dia())
            print(x.get_hora())
            print(f"Valor da inteira R$ {x.inteira():.2f}")
            print(f"Valor da meia R$ {x.meia():.2f}")
        except:
            print("Valor informado é inválido")    
    @staticmethod
    def viagem():
        pass

UI.main()


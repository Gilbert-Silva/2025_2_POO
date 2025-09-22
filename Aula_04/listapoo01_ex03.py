class Conta:
    def __init__(self):               # Construtor
        self.titular = "sem nome"     # Atributos
        self.numero = "sem número"
        self.saldo = 0
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo -= valor

class UI:
    def main():
        x = Conta() # uma instância
        print(x.titular, x.numero, x.saldo)
        x.titular = "Raquel"
        x.numero = "123-x"
        x.saldo = 1000
        print(x.titular, x.numero, x.saldo)
        x.depositar(500)  # self = x   Conta.depositar(x, 500)
        print(x.titular, x.numero, x.saldo)
        z = x # z é uma referência para a mesma instância que x referencia
        z.depositar(500)
        print(x.titular, x.numero, x.saldo)
        y = Conta() # outra instância
        y.titular = "Thiago"
        y.numero = "456-x"
        y.saldo = 2000
        print(y.titular, y.numero, y.saldo)
        y.depositar(300)
        print(y.titular, y.numero, y.saldo)
        contas = [x, y]
        contas[0].depositar(500)
        print(x.titular, x.numero, x.saldo)
        print(contas)

UI.main()

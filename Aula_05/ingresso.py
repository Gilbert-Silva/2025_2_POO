class Ingresso:            # entidade - tem instâncias
    def __init__(self):
        self.__dia = "dom"   # definição dos atributos
        self.__hora = 17
    def inteira(self):     # método de instância. self é a instância que chamou a operação
        if self.__dia == "qua": return 8
        if self.__dia in ["seg", "ter", "qui"]: valor = 16
        else: valor = 20
        if self.__hora == 0 or self.__hora >= 17: valor *= 1.5
        return valor 
    def meia(self):
        if self.__dia == "qua": return 8
        return self.inteira()/2

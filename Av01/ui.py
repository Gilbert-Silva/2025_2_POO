from pessoa import Pessoa, PessoaDAO
from corrida import Corrida, CorridaDAO
from datetime import datetime, timedelta

class UI: # classe estática -> não tem instância     
    def menu():
        print("Pessoas")
        print("1-Inserir, 2-Listar, 3-Pesquisar")
        print()
        print("Corridas")
        print("4-Inserir, 5-Listar, 6-Menor Pace")
        print()
        print("9 - Fim")
        return int(input("Informe uma opção: "))           
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.pessoa_inserir()
            if op == 2: UI.pessoa_listar()
            if op == 3: UI.pessoa_pesquisar()

            if op == 4: UI.corrida_inserir()
            if op == 5: UI.corrida_listar()
            if op == 6: UI.corrida_menor_pace()

    def pessoa_inserir():
        #id = int(input("Informe o id: "))
        id = 0
        nome = input("Informe o nome: ")
        nasc = input("Informe a data de nascimento: ")
        c = Pessoa(id, nome, datetime.strptime(nasc, "%d/%m/%Y"))
        PessoaDAO.inserir(c)
    def pessoa_listar():
        for obj in PessoaDAO.listar():
            print(obj)       
    def pessoa_pesquisar():
        nome = input("Informe o nome: ")
        pessoas = PessoaDAO.listar()
        for obj in pessoas:
            if obj.get_nome().startswith(nome): print(obj)
    def corrida_inserir():
        id = 0
        UI.pessoa_listar()
        id_pessoa = int(input("Informe o id da pessoa: "))
        data = input("Informe a data: ")
        dist = int(input("Informe a distância em metros: "))
        temp = input("Informe o tempo em hh:mm:ss: ")
        h,m,s = map(int, temp.split(":"))
        c = Corrida(id, id_pessoa, datetime.strptime(data, "%d/%m/%Y"),\
                dist, timedelta(hours=h, minutes=m, seconds=s))
        CorridaDAO.inserir(c)
    def corrida_listar():
        for obj in CorridaDAO.listar():
            print(obj)       
    def corrida_menor_pace():
        corridas = CorridaDAO.listar()
        m = corridas[0]
        for obj in corridas:
            if obj.pace() < m.pace(): m = obj
        print(m)       

UI.main()


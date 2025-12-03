try:
    a = int(input("Informe o dividendo: "))
    b = int(input("Informe o divisor: "))
    print(a/b)
#except Exception:  Exception tem que ser o último
#    print("Deu erro")    
except ValueError:
    print("Informe números inteiros")
except ZeroDivisionError:
    print("Informe um divisor não nulo")
except Exception:
    print("Deu erro")    


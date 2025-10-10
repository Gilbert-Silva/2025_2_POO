from datetime import datetime, timedelta

x = datetime.strptime("10/10/2025 9:00", "%d/%m/%Y %H:%M")
y = timedelta(hours=1, minutes=30)
z = x + y

print(x)
print(y)
print(z)

a = datetime.strptime(input("informe a data de nascimento: "), "%d/%m/%Y")
b = datetime.now()
x = b - a
print(x)
print(x.days // 365)
print(x.days % 365 // 30)


                      

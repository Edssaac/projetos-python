# Crivo de Eratóstenes
import math

num = int(input("Entre com o valor: "))
lista = []

for i in range(2, num+1):
    lista.append(i)

for x in lista:
    if x <= int(math.sqrt(num)):
        for y in lista:
            if y % x == 0 and y != x:
                lista.remove(y)
    else:
        break                    


print(lista)
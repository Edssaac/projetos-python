# Faça um programa que receba inicialmente um número n que determina o número de entradas dele.
# Após receber estas n entradas, printe eles na ordem reversa em que foram inseridas, todas na mesma
# linha.

num = int(input("Entradas desejadas: "))
lista = []

for i in range(0, num):
    var = input("Valor: ")
    lista.append(var)

lista.reverse()
for i in range(0, num):
    print(lista[i], end=" ")


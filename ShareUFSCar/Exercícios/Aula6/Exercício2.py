# Faça um programa que receba inicialmente um número n que determina o número de entradas dele.
# Após receber estas n entradas recebe uma outra entrada adicional contendo um número.
# Então printe o número de ocorrências deste número na lista.

num = int(input("Número desejado de entradas: "))
lista = []

for i in range(0, num):
    var = int(input("Valor: "))
    lista.append(var)

proc = int(input("Número a ser procurado: ")) 

pes = 0
for i in range(0, len(lista)):

    if lista[i] == int(proc):
        pes += 1

print("Total de itens encontrados:", pes)
# Faça um programa que receba um número n inicialmente que determina o número de entradas dele.
# Após receber estas n entradas seu programa deve receber um caractere que determina uma de três
# operações, que são:
# M = Media dos números inseridos
# P = quantidade de números pares
# I = quantidade de números ímpares
# Por exemplo, para um execução que insere os seguintes 5 números:
# [3, 7, 8, 5, 12]
# A opção M deve printar na tela sua média, no caso 7
# A opção P deve printar a quantidade de números pares, no caso 2
# A opção I deve printar a quantidade de números ímpares, no caso 3.

num = int(input("Número de entradas: "))
lista = []
media = 0
pares = 0
impares = 0

for i in range(0, num):
    var = int(input("Valor: "))
    lista.append(var)

print("\nEscolha:\n[M] Média\n[P] Pares\n[I] Impar")
resp = input("Desejo: ")

if resp == "M":
    for i in range(0, num):
        media += lista[i]
    media = media/len(lista)
    print(media)

elif resp == "P":
    for i in range(0, num):
        if lista[i]%2 == 0:
            pares += 1
    print(pares)

elif resp == "I":
    for i in range(0, num):
        if lista[i]%2 == 1:
            impares += 1
    print(impares)

else:
    print("Valor inválido.")        

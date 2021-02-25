# Faça um programa que receba números inteiros e armazene em um dicionário uma
# chave com este número e seu quadrado como valor dessa chave, ao final, printe este
# dicionário. Você deve ler entradas até que o número inserido pelo usuário seja 0.

d = {}
# l = []

# while True:
#     n = int(input("Digite um número: "))

#     if n != 0: 
#         l.append(n) 
#     else: break

# for i in range(0, len(l)):
#     pass
#     d[l[i]] = l[i]*l[i]

# print(d)

while True:
    n = int(input("Digite um número: "))

    if n == 0:
        print(d)
        break
    else: d[n] = n*n 
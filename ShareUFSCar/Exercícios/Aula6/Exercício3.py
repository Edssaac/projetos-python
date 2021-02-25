# Faça um programa que receba 5 valores para um lista A e 5 valores para um lista B, depois construa
# uma lista C que intercala valores de A e B. Por exemplo
# A = [5, 1, 7, 6, 12] e B = [4, 3, 9, 10, 0]
# C = [5, (1o valor de A), 4 (1o valor de B), 1(2o valor de A), 3 (2o valor de B), ...]

print("Insira valores - Lista A")
listaA = []

for i in range(0, 5):
    var = int(input("Valor: "))
    listaA.append(var)

print("Insira valores - Lista B")
listaB = []

for i in range(0, 5):
    var = int(input("Valor: "))
    listaB.append(var) 

listaC = []    
for i in range(0, 5):
    listaC.append(listaA[i])
    listaC.append(listaB[i])

print(listaC)    
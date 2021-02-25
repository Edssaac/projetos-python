# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

print ("---Sequência de Fibonacci---")
print("Deseja obter quantos valores?")
N = int(input())
n = 3
t1 = 0
t2 = 1

print (t1, t2, end=" ")

while n <= N:

    tx = t1 + t2
    print(tx, end=" ")
    t1 = t2
    t2 = tx 
    n = n + 1

input("\ndigite ENTER para finalizar...")


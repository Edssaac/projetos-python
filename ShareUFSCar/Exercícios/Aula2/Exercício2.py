"""" 2. Faça um programa que receba dois nomes e um número inteiro e então imprima os
seguintes dados:
- Concatenação dos dois nomes
- O primeiro nome concatenado n vezes, sendo que n é o número inteiro colocado
como entrada """

print("Digite dois nomes e um número.")
nome = input()
nome2 = input()
num = int(input())

print(nome, nome2, num)
print("\nConcatenação:")
print(nome + nome2)
print("\nConcatenação Multipla:")
print(nome * num)

input("Pressione ENTER para encerrar")
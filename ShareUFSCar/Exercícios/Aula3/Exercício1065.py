# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

print("Digite o primeiro valor:")
a = int(input())

print("Digite o segundo valor:")
b = int(input())

print("Digite o terceiro valor:")
c = int(input())

print("Digite o quarto valor:")
d = int(input())

print("Digite o quinto valor:")
e = int(input())

resp = int
resp = 0

if (a % 2 == 0):
    resp = (resp + 1)

if (b % 2 == 0):
    resp = (resp + 1)

if (c % 2 == 0):        
    resp = (resp + 1)

if (d % 2 == 0):
    resp = (resp + 1)

if (e % 2 == 0):
    resp = (resp + 1)      

print("O total de números pares é:", resp)

input("digite ENTER para finalizar...")

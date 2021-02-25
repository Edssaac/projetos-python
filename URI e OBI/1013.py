# O Maior

# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. 

a, b, c = map(int, input().split())

print("{} eh o maior".format(max(a, b, c)))
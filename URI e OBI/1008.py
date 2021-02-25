# Salário

# Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

n = int(input())
nh = int(input())
vh = float(input())

t = (nh * vh)

print("NUMBER = {}\nSALARY = U$ {}".format(n, "%0.2f" %t))
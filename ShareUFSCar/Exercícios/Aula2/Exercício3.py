""" 3. Faça um programa que faça o cálculo de uma equação quadrática dados os
coeficientes e o valor x como entrada.
A fórmula de qualquer expressão quadrática é: f(x) = ax2 + bx + c
Seu programa deve receber como entrada estes coeficientes a, b e c assim como o
valor x. """

print("Temos a função: f(x) = ax2 + bx + c")
print("Insira de forma sequencial os valores de: a, b, c, x:")
a = int(input())
b = int(input())
c = int(input())
x = int(input())
print(a, b, c, x)

resultado = a*(x**2) + (b*x) + (c)
print("\nA função tem como resultado:", resultado)

input("Pressione ENTER para encerrar")
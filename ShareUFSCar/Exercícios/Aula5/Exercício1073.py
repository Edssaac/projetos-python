# Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

x = int(input())

for i in range(1, x+1):
    
    if i%2 == 0:
        print(i, "^", "2 =", i**2)

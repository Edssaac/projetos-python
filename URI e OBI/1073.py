# Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.

# N = int(input("N: "))

# for i in range(1, N+1):
#     if i % 2 == 0: 
#         print(f"{i}^2 =", (i **2))

# Versão do Professor:
n = int(input())

for i in range(1, n+1):
    if i % 2 ==0:
        print("{}^2 = {}".format(i, i*i))
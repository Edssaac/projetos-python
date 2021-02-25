# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

# N = int(input("Quantidade: "))

# for i in range(N):
#     X, Y = map(int, input("Valores: ").split())
#     maior = max(X, Y)
#     menor= min(X, Y)

#     soma = 0
#     for c in range(menor+1, maior):
#         if c % 2 == 1:
#             soma += c
#     print(soma)



# Versão do Professor:
n = int(input())

for i in range(n):
    linha = [int(num) for num in input().split()]
    x = min(linha)
    y = max(linha)

    soma = 0
    for num in range(x+1, y):
        if num % 2 == 1:
            soma += num

    print(soma)

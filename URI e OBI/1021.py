# Notas e Moedas

# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.


# Minha Versão:
N = float("%.2f" %float(input()))

n100 = n50 = n20 = n10 = n5 = n2 = n1 = n050 = n025 = n010 = n05 = n01 = 0 

while (N > 0):
    N = float("%.2f" %N)

    if (N >= 100):
        n100 += 1
        N -= 100
    elif (N >= 50):
        n50 += 1
        N -= 50 
    elif (N >= 20):
        n20 += 1
        N -= 20
    elif (N >= 10):
        n10 += 1
        N -= 10
    elif (N >= 5):
        n5 += 1
        N -= 5
    elif (N >= 2):
        n2 += 1
        N -= 2

    elif (N >= 1):
        n1 += 1
        N -= 1
    elif (N >= 0.50):
        n050 += 1
        N -= 0.50
    elif (N >= 0.25):
        n025 += 1
        N -= 0.25
    elif (N >= 0.10):
        n010 += 1
        N -= 0.10
    elif (N >= 0.05):
        n05 += 1
        N -= 2
    elif (N >= 0.01):
        n01 += 1
        N -= 0.01
N = 0

print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(n100))
print("{} nota(s) de R$ 50.00".format(n50))
print("{} nota(s) de R$ 20.00".format(n20))
print("{} nota(s) de R$ 10.00".format(n10))
print("{} nota(s) de R$ 5.00".format(n5))
print("{} nota(s) de R$ 2.00".format(n2))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(n1))
print("{} moeda(s) de R$ 0.50".format(n050))
print("{} moeda(s) de R$ 0.25".format(n025))
print("{} moeda(s) de R$ 0.10".format(n010))
print("{} moeda(s) de R$ 0.05".format(n05))
print("{} moeda(s) de R$ 0.01".format(n01))


# Como remover centavos
# n = 10.45

# while True:
#     print(n)
#     n = n - 0.01
#     n = float("%.2f" %n)
#     print(n)





# Versão Assistida
# N = float(input())
# notas = [100, 50, 20, 10, 5, 2]
# moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

# print("NOTAS:")
# for nota in notas:
#     qtd_nota = int(N / nota)
#     print("{} nota(s) de R$ {:.2f}".format(qtd_nota, nota))
#     N -= (qtd_nota * nota)

# print("MOEDAS:")
# for moeda in moedas:
#     qtd_moeda = int(round(N, 2) / moeda)
#     print("{} moeda(s) de R$ {:.2f}".format(qtd_moeda, moeda))
#     N -= (qtd_moeda * moeda)






# Versão Aceita:
# n = float(input())

# n100 = n // 100
# n = n - n100*100

# n50 = n // 50
# n = n - n50*50

# n20 = n // 20
# n = n - n20*20

# n10 = n // 10
# n = n - n10*10

# n5 = n // 5
# n = n - n5*5

# n2 = n // 2
# n = n - n2*2

# n1 = n // 1
# n = n - n1*1
# n1=float('%.2f'% n1)
# n=float('%.2f'% n)

# m50 = n // 0.5
# n = n - m50*0.5
# m50=float('%.2f'% m50)
# n=float('%.2f'% n)

# m25 = n // 0.25
# n = n - m25*0.25
# m25=float('%.2f'% m25)
# n=float('%.2f'% n)

# m10 = n // 0.10
# n = n - m10*0.10
# m10=float('%.2f'% m10)
# n=float('%.2f'% n)

# m5 = n // 0.05
# n = n - m5*0.05
# m5=float('%.2f'% m5)
# n=float('%.2f'% n)

# m1 = n * 100
# m1=float('%.2f'% m1)
# n=float('%.2f'% n)

# print('NOTAS:')
# print('{} nota(s) de R$ 100.00'.format(int(n100)))
# print('{} nota(s) de R$ 50.00'.format(int(n50)))
# print('{} nota(s) de R$ 20.00'.format(int(n20)))
# print('{} nota(s) de R$ 10.00'.format(int(n10)))
# print('{} nota(s) de R$ 5.00'.format(int(n5)))
# print('{} nota(s) de R$ 2.00'.format(int(n2)))
# print('MOEDAS:')
# print('{} moeda(s) de R$ 1.00'.format(int(n1)))
# print('{} moeda(s) de R$ 0.50'.format(int(m50)))
# print('{} moeda(s) de R$ 0.25'.format(int(m25)))
# print('{} moeda(s) de R$ 0.10'.format(int(m10)))
# print('{} moeda(s) de R$ 0.05'.format(int(m5)))
# print('{} moeda(s) de R$ 0.01'.format(int(m1)))
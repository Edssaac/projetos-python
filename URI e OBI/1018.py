# Cédulas

# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

y = x = int(input())
# 100 - 50 - 20 - 10 - 5 - 2 - 1
cem = cinq = vint = dez = cinc = ds = um = 0

while (y > 0):
    if (y >= 100):
        cem += 1
        y -= 100
    elif (y >= 50):
        cinq += 1
        y -= 50
    elif (y >= 20):
        vint += 1
        y -= 20
    elif (y >= 10):
        dez += 1
        y -= 10
    elif (y >= 5):
        cinc += 1
        y -= 5
    elif (y >= 2):
        ds += 1
        y -= 2
    elif (y >= 1):
        um += 1
        y -= 1
    # print(y)

print(x)
print("{} nota(s) de R$ 100,00".format(cem))
print("{} nota(s) de R$ 50,00".format(cinq))
print("{} nota(s) de R$ 20,00".format(vint))
print("{} nota(s) de R$ 10,00".format(dez))
print("{} nota(s) de R$ 5,00".format(cinc))
print("{} nota(s) de R$ 2,00".format(ds))
print("{} nota(s) de R$ 1,00".format(um))
# Lanche

# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

a, b = map(int, input().split())
cod = [1, 2, 3, 4, 5]
valor = [4.00, 4.50, 5.00, 2.00, 1.50]

for i in range(0, 5):
    if (a == cod[i]):
        total = valor[i] * b

print("Total: R$ {:.2f}".format(total))
# Salário com Bônus

# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

nome = str(input())
sf = float(input())
tv = float(input())

t = sf + ((tv * 15) / 100)

print("TOTAL = R$ {}".format("%.2f" %t))
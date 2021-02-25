# Intervalo

# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

# O símbolo ( representa "maior que". Por exemplo:
# [0,25]  indica valores entre 0 e 25.0000, inclusive eles.
# (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000 

N = float(input())

if (N >= 0 and N <= 25):
    print("Intervalo [0,25]")
elif (N > 25 and N <= 50):
    print("Intervalo (25,50]")
elif (N > 50 and N <= 75):
    print("Intervalo (50,75]")
elif (N > 75 and N <= 100):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
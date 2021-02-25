# Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.
print ("---Fatorial---")
num = int(input("Insira um valor: "))
num2 = num
resul = 1


while num >= 1:

    resul = resul * num

    num = num - 1

print ("O Fatorial de " + str(num2) + " é: " + str(resul))
input("digite ENTER para finalizar...")

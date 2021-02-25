# Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.

total = int(input("Deseja insereir quantos números? "))
i = 0

while total > 0 and i < total:
    valor = int(input("Valor: "))
    if valor % 2 == 0 and valor > 0:
        print ("EVEN POSITIVE")
    elif valor % 2 == 0 and valor < 0:
        print ("EVEN NEGATIVE")
    elif valor % 2 == 1 and valor > 0:
        print ("ODD POSITIVE")
    elif valor % 2 == 1 and valor < 0:
        print ("ODD NEGATIVE")        
    else:
        print ("NULL")

    i += 1

print ("Processo Finalizado!") 
input ("digite ENTER para finalizar...")   
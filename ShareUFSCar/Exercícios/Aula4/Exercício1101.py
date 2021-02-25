# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

print('Digite quantos pares desejar:')

while True:
    M, N = map(int,input().split(" ")) # map(int,input().split(" ")) possibilita a leitura de mais de um valor (relativo as variaveis impostas) 

    if M <= 0 or N <= 0:
        break
    
    if M > N:
        Maior = M
        Menor = N

    if N > M:
        Maior = N
        Menor = M         

    soma = 0
    while not Menor > Maior:
        print(Menor, end=" ") #end="" possibilita a quebra de linha.
        soma = soma + Menor
        Menor += 1

    print("Soma:", soma)

input("digite ENTER para finalizar...")



# print('t', end="")
# print('e', end="")
# print('s', end="")
# print('t', end="")
# print('e')
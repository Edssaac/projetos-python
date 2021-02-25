# Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

x = int(input())

for i in range(0, 10000):

    if i % x == 2:
        print(i)
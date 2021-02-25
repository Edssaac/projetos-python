    # Na matemática, um Número Primo é aquele que pode ser dividido somente por 1 (um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido apenas pelo número 1 e pelo número 7.

x = int(input())

for i in range(0, x):
    n = int(input())
    a = 0
    b=1

    while b <= n:
        if n % b == 0:
            a += 1
        b += 1

    if a > 2:
        print(n, "não é primo")
    else:
        print(n, "é primo")
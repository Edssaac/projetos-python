def collatz(n):
    if (n % 2) == 0:
        n = n / 2
    else:
        n = (3 * n) + 1

    return int(n) 


n = int(input("Digite o primeiro número da sequência: "))
print(n)

while n != 1:
	n = collatz(n)
	print(n)
# Sort Simples

# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

valores = input().split()
val = [int(i) for i in valores]

val.sort()

print(*val, sep="\n")
print("")
print(*valores, sep="\n")
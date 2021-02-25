# Múltiplos

# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

A, B = map(int, input().split())

if ( (max(A,B) % min(A,B)) == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")


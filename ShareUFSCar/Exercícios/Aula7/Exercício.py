A = []
B = []

x = 1
xa = int(input("Quantidade desejada a ser inserida em A: "))
for i in range(0, xa):
    a = int(input(str(x) + "#: "))
    A.append(a)
    x += 1

x = 1
xb = int(input("Quantidade desejada a ser inserida em B: "))
for i in range(0, xb):
    b = int(input(str(x) + "#: "))
    B.append(b)
    x += 1

if (len(A) == 0):
    A.append(0)
if (len(B) == 0):
    B.append(0)

print("\n           OPÇÕES")
print("[0] - Sair do programa")
print("[1] - Exibir a soma dos valores de A ou B")
print("[2] - Exibir a soma geral dos dois vetores")
print("[3] - Exibir a média dos valores de A ou B")
print("[4] - Exibir a média geral")
print("[5] - Exibe o maior valor de A ou B")
print("[6] - Exibe o maior valor geral")
print("[7] - Exibe o menor valor de A ou B")
print("[8] - Exibe o menor valor geral")
print("[9] - Exibe todos os valores de A ou B")
print("[10] - Exibe todos os valores de A ou B em ordem inversa")
print("[11] - Exibe todos os valores pares de A ou B")
print("[12] - Exibe todos os valores ímpares de A ou B")
print("[13] - Exibe todos os valores primos de A ou B")

esc = int(input(("\n Opção Escolhida: ")))

x = 0
if (esc == 0):
    exit

elif (esc == 1):
    ab = int(input("[0]A ou [1]B: "))
    if (ab == 0):
        x = sum(A)

        print("Temos como a soma dos valores de A:", x)
    if (ab == 1):
        x = sum(B)

        print("Temos como a soma dos valores de B:", x)  

elif (esc == 2):
    x = sum(A) + sum(B)

    print("Temos como a soma geral:", x)  

elif (esc == 3):
    ab = int(input("[0]A ou [1]B: "))
    if (ab == 0):
        x = sum(A) / len(A)
        print("Temos como a média de A:", x)
    if (ab == 1):
        x = sum(B) / len(B)
        print("Temos como a média de B:", x)  

elif (esc == 4):
    x = (sum(A) + sum(B)) / (len(A) + len(B))
    print("Temos como a média geral:", round(x, 2)) 

elif (esc == 5):
    ab = int(input("[0]A ou [1]B: "))
    if (ab == 0):
        x = max(A)

        print("Temos como o maior valor de A:", x)
    if (ab == 1):
        x = max(B)

        print("Temos como o maior valor de B:", x) 

elif (esc == 6):
    x = max(A)
    y = max(B)

    if (x >= y):
        x = max(A)
    else:        
        x = max(B)

    print("Temos como o maior valor geral:", x) 

elif (esc == 7):
    ab = int(input("[0]A ou [1]B: "))
    if (ab == 0):
        x = min(A)

        print("Temos como o menor valor de A:", x)
    if (ab == 1):
        x = min(B)

        print("Temos como o menor valor de B:", x)

elif (esc == 8):
    x = min(A)
    y = min(B)

    if (x <= y):
        x = min(A)
    else:        
        x = min(B)

    print("Temos como o menor valor geral:", x) 

elif (esc == 9):
    ab = int(input("[0]A ou [1]B: "))
    if (ab == 0):
        print("A: ", end="")
        for i in range(0, len(A)):
            print(A[i], end=" ")
    if (ab == 1): 
        print("B: ", end="")
        for i in range(0, len(B)):
            print(B[i], end=" ")

elif (esc == 10):
    A.reverse()
    B.reverse()
    ab = int(input("[0]A ou [1]B: "))
    if (ab == 0):
        for i in range(0, len(A)):
            print(A[i], end=" ")
    if (ab == 1): 
        for i in range(0, len(B)):
            print(B[i], end=" ")

elif (esc == 11):
    ab = int(input("[0]A ou [1]B: "))
    if (ab == 0):
        print("Temos como os valores pares em A: ", end="")
        for i in range(0, len(A)):
            if (A[i] % 2 == 0):
                print(A[i], end=" ")
    if (ab == 1): 
        print("Temos como os valores pares em B: ", end="")
        for i in range(0, len(B)):
            if (B[i] % 2 == 0):
                print(B[i], end=" ")

elif (esc == 12):
    ab = int(input("[0]A ou [1]B: "))
    if (ab == 0):
        print("Temos como os valores ímpares em A: ", end="")
        for i in range(0, len(A)):
            if (A[i] % 2 == 1):
                print(A[i], end=" ")
    if (ab == 1): 
        print("Temos como os valores ímpares em B: ", end="")
        for i in range(0, len(B)):
            if (B[i] % 2 == 1):
                print(B[i], end=" ")

elif (esc == 13):
    ab = int(input("[0]A ou [1]B: "))
    if (ab == 0):
        print("Temos como valores primos em A: ", end="")
        for c in range(0, len(A)):
            z = A[c]
            y = 0
            for i in range(1, z+1):
                if z % i == 0:
                    y += 1
            if y == 2:
                print(z, end=" ") 
    if (ab == 1):
        print("Temos como valores primos em B: ", end="")
        for c in range(0, len(B)):
            z = B[c]
            y = 0
            for i in range(1, z+1):
                if z % i == 0:
                    y += 1
            if y == 2:
                print(z, end=" ")

else:
    print("Opção Inválida")  
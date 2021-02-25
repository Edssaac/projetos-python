# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

# N = int(input("Quantidade: "))
# X = []
# a = b = 0

# for i in range(1, N+1):
#     x = int(input(f"Valor #{i}: "))
#     X.append(x)  

# for i in range(0, len(X)):
#     if (X[i] < 10) or (X[i] > 20):
#         a += 1
#     else:
#         b += 1        

# print(f"{a} in\n{b} out")    



# Versão do Professor:
# n = int(input())

# dentro = 0
# fora = 0

# for i in range(n):
#     num = int(input())

#     if 10 <= num <= 20:
#         dentro += 1
#     else:
#         fora += 1

# print("{} in".format(dentro))        
# print("{} out".format(fora))        



# Minha versão Aprimorada:
N = int(input("Quantidade: "))
a=b=0
c=1

for i in range(N):
    X = int(input(f"Valor #{c}: "))

    if 10 <= X <= 20:
        a += 1
    else:
        b += 1
    c += 1

print()    
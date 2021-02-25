# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

print("Digite o valor de A:")
A = int(input())

print("Digite o valor de B:")
B = int(input()) 

print("Digite o valor de C:")
C = int(input()) 

print("Digite o valor de D:")
D = int(input()) 

if (B > C and D > A and (C + D) > (A + B)):
    C = (C % 2)
    D = (D % 2)
    if (C == 0 and D == 0):
        print("Valores aceitos!")
else:
    print("Valores não aceitos!")

input("digite ENTER para finalizar...")              
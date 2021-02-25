# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

print("Digite A:")
A = int(input())

print("Digite B:")
B = int(input())


if (A > B):
    if (A % B == 0):
        print("São múltiplos.")
    else:
        print("Não são múltiplos.")   

if (A < B):    
       if (B % A == 0):
        print("São múltiplos.")
       else:
        print("Não são múltiplos.")

if (A == B):
    print("São múltiplos.")        


input("digite ENTER para finalizar...")
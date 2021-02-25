# "for"


# Percorre cada letra da váriavel tipo string
# string = "casa"

# for i in string:
#     print (i)


#  Não posso fazer o mesmo com números (int/float)
# string = 23

# for i in string:
#     print (i)    


# Podemos usar o for com listas (arrays)
# lista = ["abacate", "melão", "uva", "morango"]

# print ("Vou ao hortifruti comorar:")
# for compras in lista:
#     print(compras) 


# for e range()
# for i in range(0,5):
#     print (i) # Será impresso os números de 0 até 4, pois o range vai até a casa anterior ao segundo valor escolhido. 


# Fibonacci
# n = int(input())

# a = 0
# b = 1
# print (a, end=" ")
# print (b, end=" ")
# for i in range(0, n-2):
#     c = a+b
#     print (c, end=" ")
#     a = b
#     b = c


# Como fica usando o bloco "while"?
# n = int(input())

# a = 0
# b = 1
# print (a, end=" ")
# print (b, end=" ")

# i = 0
# while i < n-2:
#     c = a+b
#     print (c, end=" ")
#     a = b
#     b = c 

#     i += 1


# Lendo essa bagaça
# m = int(input())
# n = int(input())
# while (m != 0 and n != 0):
#     if m > n:
#         maior = m
#         menor = n
#     else:
#         maior = n
#         menor = m

#     soma = 0
#     for i in range(menor, maior + 1):
#         print (i, end=" ")
#         soma += i

#     print ("soma:", soma)

#     m = int(input())
#     n = int(input())


#  Maior e posição
# maior  = 0
# print("Digite números:")
# for i in range(0,5):
#     x = int(input())

#     if x  > maior:
#         maior = x 
#         pos = i + 1
 
# print("O maior número digitado é o:", maior)
# print("E ele se encontra na posição:", pos)


# Tabuada
# n = int(input())

# for i in range(1,11):
#     print(i, "X", n, "=", i*n ) 


# Senha
print("Digite a senha correta:")
senha = int(input())

while (senha != 2002):
    print("Senha incorreta! Tente novamente.")
    senha = int(input())

print ("Acesso permitido")
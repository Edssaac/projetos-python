# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
import math 

print("- Bhaskara -")

# A, B, C = input().split(" ")
# A = float(A)
# B = float(B)
# C = float(C)

# if (A == 0):
#     print("Impossivel calcular!")
#     exit()

# X = ((B) ** 2) - 4 * (A) * (C)  

# if (X < 0):
#     print("Impossivel calcular!")
#     exit()

# X = math.sqrt(X)

# x1 = (-(B) + (X)) / (2 * (A))
# x2 = (-(B) - (X)) / (2 * (A))


# print("R1 = %.5f" %x1)
# print("R2 = %.5f" %x2)



# Versão do Professor:
# entrada = input()
# entrada = entrada.split() # Pode ser usado para separar os valores das listas

# print(entrada)

entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

delta = b * b - 4 * a * c

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)   
    x2 = (-b - math.sqrt(delta)) / (2*a) 
    print("R1 = %0.5f" %x1)
    print("R2 = %0.5f" %x2)
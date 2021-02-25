# Condicionais
# CTRL + ;

# Operação !=
# a = 3
# b = 4

# if (a == 3):
#     print("a é igual a 3") 
#     if (b != 5):
#         print("b é diferente de 5")

# Operação ==
# a = 3
# b = 5

# if (a == 3):
#     print("a é igual a 3") 
#     if (b == 5):
#         print("b é igual a 5")

# Operação not
# a = 2
# b = 5

# if (not a == 3):
#     print("a é igual a 3") 
#     if (b == 5):
#         print("b é igual a 5")

# Operação > e <
# a = 2
# b = 15

# if (a < 3):
#     print("a é igual a 3") 
#     if (b > 5):
#         print("b é igual a 5")

# Operação and e Operação or
# a = 2
# b = 15

# if (a < 3 and a != 1):
#     print("a é igual a 3 e diferente de 1") 
#     if (b > 5 or b < 20 ):
#         print("b é igual a 5") 

# Operação <= e >=

# a = 4
# b = 5
# c = 7

# if ((a > 3 and b == 5) or (c == 6 and b == 5)):
#     print("tudo isso ai")

# elif e else

# a = 2

# if (a == 1):
#     print("a = 1")
# elif (a == 3):
#     print("a = 3") 
# else:
#     print("e eu vou saber?") 

# a = input("Você está bem? (sim/não): ")

# if (a == "SIM" or a == "sim" or a == "Sim"):
#     print("que bom!")
# elif (a == "NÃO" or a == "não" or a == "Não" or a == "NAO" or a == "nao" or a == "Nao" ):
#     print("poxa que pena")
# else:
#     print("#408 Resposta Inválida!") 

print("Digite um número: ")
num = int(input()) 

resp = (num % 2)

if (resp == 0):
    print("O número", num, "é par!")
elif (resp == 1):
    print("o número", num, "é impar!") 
        
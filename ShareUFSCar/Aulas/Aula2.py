# Variáveis e seus tipos: Int/Float/Str
num = 3
num2 = 13.98
isnotnum = "abacate"

print("O meu número favorito é:", num)
print("O meu segundo número favorito é:", num2)
print("A minha palavra favorita é:", isnotnum)
print(type(isnotnum)) #type tem a função de nos dizer que o tipo da var.
print("\n")

#Operações algébricas:
print(num+num2) #Adição
print(num-num2) #Subtração
print(num*num2) #Multiplicação
print(num/num2) #Divisão
print(num**num2) #Potenciação
print(num%num2) #Módulo
print("\n")

#Operações com String:
nome = "Edson "
sobrenome = "Isaac"

print(nome + sobrenome)
print(nome*num)
print("\n")

#Entrada (Input):
nome2 = input()
a = int(input()) #Tem que ser definido como um int ou float, ou vai ser tratado como um str.
b = int(input())

print("Digite o seu nome:", nome2)
print("Digite A:", a)
print("Digite B:", b)
print("A + B:",a+b)
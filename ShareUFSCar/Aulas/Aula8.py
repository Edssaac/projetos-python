# Funções (de maneira matemática):

'''
# Ex: f(x) = x^2 + x - 1
x = int(input("f(x): "))

y =  (x ** 2) + x - 1
print(f"\nf({x}) = {x}² + {x} - 1")
print(f"f{x}: {y}")
'''



# Sintaxe:

'''
def nomeFuncao(variavel):
    codigo
# variaveis são opcionais
'''

# Exemplo:
def setFuncao(batata):
    if batata != int:
        print("kkj batatatatatata")

# setFuncao(4.9)   



# Pondo em Prática:
def f(x):
    y =  (x ** 2) + x - 1
    print(f"\nf({x}) = {x}² + {x} - 1")
    print(f"f{x}: {y}")    

# x = int(input("f(x): "))
# f(x)


# Exemplo de função sem parâmentro:
def test():
    print("8")

# test()



# return:
def soma(a, b):
    return a + b
print(soma(2, 3))
# n1 = int(input("valor 1: "))    
# n2 = int(input("valor 2: "))    

# resultado = soma(n1, n2)
# print(resultado)

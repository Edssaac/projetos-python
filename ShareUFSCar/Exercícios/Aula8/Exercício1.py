def soma(a, b):
    return (a + b)

def subtracao(a, b):
    return (a - b)

def multiplicao(a, b):
    return (a * b)

def divisao(a, b):
    return (a / b)


while True:
    print("Opções: [0] Sair [1] Soma [2] Subtração [3] Multiplicação [4] Divisão")
    opcao = int(input("Sua opção? "))

    if opcao == 0:
        break

    a = int(input("Primeiro número: "))
    b = int(input("Segundo número: "))

    if opcao == 1:
        print(soma(a, b))
    elif opcao == 2:
        print(subtracao(a, b))
    elif opcao == 3:
        print(multiplicao(a, b))
    elif opcao == 4:
        print(divisao(a, b))
    else:
        print("Opção inválida!")
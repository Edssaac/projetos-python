def inicializaLista():
    global nomes
    while True:
        x = input("Nome: ")

        if (x == "" ): break
         
        nomes.append(x)


def adicionaNome():
    global nomes
    x = input("Nome: ")
    nomes.append(x)


def removeNome():
    global nomes
    x = input("Nome: ")
    nomes.remove(x)


def buscaNome():
    global nomes
    x = input("Nome: ")
    if nomes.count(x) > 0:
        return True


def printaLista():
    global nomes
    print(*nomes, end="")
    print("\n")


nomes = []

while True:
    print("Opções:",
          "[0] Sair",
          "[1] Inicializar a lista",
          "[2] Adicionar nome a lista",
          "[3] Retirar nome da lista",
          "[4] Buscar nome na lista",
          "[5] Printar a lista"
          )

    opcao = int(input("Sua opção? "))

    if opcao == 0:
        break
    if opcao == 1:
        inicializaLista()
    elif opcao == 2:
        adicionaNome()
    elif opcao == 3:
        removeNome()
    elif opcao == 4:
        if buscaNome():
            print("O nome buscado está na lista!")
        else:
            print("O nome buscado não está na lista!")
    elif opcao == 5:
        printaLista()
    else:
        print("Opção inválida!")

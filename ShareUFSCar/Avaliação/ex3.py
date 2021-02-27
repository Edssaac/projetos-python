# nome cpf idade
def I():
    entrada = input().split()

    with open('db.txt', 'r+') as db:
        if entrada[1] in db.read(): 
            print("Erro: CPF já cadastrado!")
        else: 
            with open('db.txt', 'a') as db:
                db.write(entrada[0] + " " + entrada[1] + " " + entrada[2] + " " + "\n")


def R():
    cpf = str(input())
    with open("db.txt", "r") as arquivo:
        listas = []
        gambiarra = 0
        for line in arquivo:
            lista = []

            lista.append(line)
            listas.append(lista)
        for i in listas: 
            for k in i: 
                if cpf in k:
                    listas.remove(i)
                    gambiarra += 1

        if gambiarra == 0: print("CPF não encontrado!") 
        else:
            with open("db.txt", "w") as arquivo:
                for i in listas:
                    for k in i: 
                        arquivo.write(k)


def P():
    with open('db.txt', 'r+') as db:
        entrada = input().split()
        gambiarra = 0

        for line in db: 
            lista = []
            line = line.replace("\n", "")
            lista.append(line.split(" "))
            for i in lista:
                for k in i:
                    if entrada[1] == k: 
                        print(i[0], i[1], i[2])
                        gambiarra += 1
        
        if gambiarra == 0: print("Usuário não encontrado!") 



while True:
    comando = input()
    if comando == "I":
        I()
    elif comando == "R":
        R()
    elif comando == "P":
        P()
    elif comando == "X":
        break

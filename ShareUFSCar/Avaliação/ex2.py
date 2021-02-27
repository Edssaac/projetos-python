# Estacionamento

estacionamento = {
    0 : "",
    1 : "",
    2 : "",
    3 : "",
    4 : "",
    5 : "",
    6 : "",
    7 : "",
    8 : "",
    9 : "",
}

def add():
    if "" not in estacionamento.values(): 
        print("O estacionamento está lotado!")
    else:        
        if estacionamento[int(comando[2])] == "":
            estacionamento[int(comando[2])] = comando[1]
        else: print("Já existe um veículo nessa vaga!")

def rm():
    if comando[1] in estacionamento.values(): 
        for i in range(0, len(estacionamento)): 
            if estacionamento[i] == comando[1] :
                estacionamento[i] = ""
    else: print("Não há veículos para remover!")

def ls():
    lista = []
    for i in estacionamento.values() :
        if i == "": lista.append("Livre")
        else: lista.append("Ocupada")
    return print(lista)


while True:
    comando = input().split()

    if comando[0] == "add":
        add()
    elif comando[0] == "rm":
        rm()
    elif comando[0] == "ls":
        ls()
    elif comando[0] == "exit": break

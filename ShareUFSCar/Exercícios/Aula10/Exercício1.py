# Faça um programa que leia uma arquivo com diversas palavras separadas por um
# espaço e então conte quantas palavras cada uma tem. Seu programa deve receber o
# nome de um arquivo como entrada e então retornar quantas palavras ele tem.

try:
    name = str(input("Nome do Arquivo: "))

    file = open(name, "r")
    ctx = file.readlines()

    amount = 0
    for t in ctx:
        amount += len(t.split(" "))

    print(f"O arquivo selecionado possui um total de {amount} palavras!")
    file.close()
except:
    print("Nome inválido!")
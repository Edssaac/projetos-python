# Faça um programa que copie arquivos.
# Seu programa deve receber o nome de um arquivo como entrada e então criar um
# novo arquivo cópia, com o mesmo conteúdo que o primeiro e um nome ligeiramente
# diferente, como no exemplo a baixo.
from random import choice, randint

try:
    name = str(input("Nome do arquivo: "))

    file = open(name, "r")
    ctx = file.read()

    newName = choice(["a", "b", "c", "d", "e", "f"]) + str(randint(0, 1023)) + "txt"
    file2 = open(newName, "x")

    file2.write(ctx)

    file.close()
    file2.close()
except:
    print("Nome inválido.")
# listas = usadas para grandes quantidades de váriaveis, podem ser de quaisquer tipo(int, float, str...)
# podem ser vazias.
# são do tipo <class 'list'>

# notas = [5.7, 7.2, 6.8]

# print(notas[2])



# print("Itens")

# print("0 - Abacaxi")
# print("1 - Melão")
# print("2 - Uva")
# print("3 - Morango")
# print("4 - Jaca")

# lista = ["Abacaxi", "Melão", "Uva", "Morango", "Jaca"]

# var = input("Escolha um item: ")

# print(f"Você escolheu comprar {lista[int(var)]}.") # Para escolher um ou mais itens da lista use [] após a var_lista, o valor dentro dos colchetes deve ser INT. Pode haver operações.


# var = 0

# for i in lista:
#     print(lista[int(var)])
#     var += 1



# Opções de seleção:
# itens = [13, "Abacaxi", True, 6.2]

# for i in range(0, 4):
#     print(i)

   
# var = 0
# for i in itens:
#     print(itens[int(var)])
#     var += 1


# for i in range(0, 4):
#     print(i, itens[i])


# itens = [13, "Abacaxi", True, 6.2]

# for i in range(0, len(itens)):
#     print(i, itens[i])


# notas = [6.7, 7.2, 8.7, 3.5, 1.9, 5, 9.1]
# notaAM = 0

# print("Temos as seguintes notas acima da média:")
# for i in range(len(notas)):
#     if notas[i] >= 6:
#         print(notas[i])


notas = [6.7, 7.2, 8.7, 3.5, 1.9, 5, 9.1]
notaAM = 0
notaAbM = 0
for i in range(len(notas)):
    if notas[i] >= 6:
        notaAM += 1
    else:
        notaAbM += 1
print(f"Temos um total de {notaAM} notas acima da média!")  
print(f"Temos um total de {notaAbM} notas abaixo da média!")     
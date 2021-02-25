# cores = ["vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom"]
# print (cores)
# print (type(cores))

# minha_lista = []

# cores = ["vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom"]

# print (f"0-based indexing into the list ... second item: {cores[1]}")

# print (f"Last item of the list: {cores[-1]}")

# print (f"Next to last item in the list: {cores[-2]}")

# cores = ["vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom"]

# print("\nEscrever uma FATIA, começando do index 2 e excluidndo o index 5:")
# print (cores[2:5])
# print (type(cores[2:5]))
# print("\nImprimir uma fatia, começando do index 0 até o index 3:")
# print(cores[:3])
# print("\nImprimir uma fatia, começando do index 4 até o fim da lista:")
# print(cores[4:])
# print("\nImprimir ma fatia, do quarto último até o fim da lista:")
# print(cores[-4:-1])

cores = ["vermelho", "verde", "azul", "amarelo", "laranja", "roxo", "marrom"]
cores.reverse()
print(cores)
cores.sort()
print(cores)

cores.append('black')
cores.append('white')

cores.remove('yellow')
cores.remove('orange')

print(cores)

new_colors = ['lime', 'gray']
cores.extend(new_colors)
print(cores)

cores.clear()
print(cores)
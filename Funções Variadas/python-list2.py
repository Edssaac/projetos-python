# numbers = [1, 3, 5]

# print (5 in numbers)
# print (8 in numbers)
# print (5 not in numbers)
# print (8 not in numbers)

# cities = ["Chicago", "London", "Tokyo"]

# for city in cities:
#     print(city)

# numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
# numbers.sort()

# for number in numbers:
#     if number > 42:
#         break
#     print(number)

# import random
# numbers = []

# while len(numbers) < 5:
#     numbers.append(random.randint(1, 100))

# for number in numbers:
#     print(number)
#     if number >= 90:
#         print("Foi encontrado pelo menos um número maior do que 90.")
#         break
# else:
#     print("Nenhum número maior do que 90.")   

# print("Completo")

# valores = ["Casa", 10, "Prédio", 35, "Apartamento", 67]
# construc = []

# for valor in valores:
#     if isinstance(valor, str) == False:
#         continue
#     construc.append(valor)

# print(construc)    

# suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
# ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

# for  suit in suits:
#   for rank in ranks:
#     print(f'{rank} of {suit}')

import random

numbers = [42, 77, 16, 101, 23, 8, 4, 15, 55]
selected_number = random.choice(numbers)
print(selected_number)

selected_numbers = random.choices(numbers, k=4)
print(selected_numbers)
import random
deck = []
mjogador = []

suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

for  suit in suits:
  for rank in ranks:
    deck.append(f'{rank} of {suit}')

print (f"O baralho possui {len(deck)} cartas.")
print("Distribuindo")

while len(mjogador) < 5:
    aa = (random.choice(deck))
    deck.remove(aa)
    mjogador.append(aa)

print(f"O baralho possui {len(deck)} cartas.")
print("O jogador possui as seguintes cartas:")
print(mjogador)
#pop = remover item da lista. Seu oposto é o append
# pop()  = seleciona pelo INDICE  <<<

"""
print("             Lista")

lista = ["abacate", "banana", "cenoura", "danone", "espinafre"]
valor = 0
for i in lista:
    print(valor, i)
    valor = valor + 1

x = int(input("Escolha um para ser removido: ")) 

lista.pop(x) #Se não houver um número requisitado ou definido, o item a ser removido será o último da lista.

print("A lista atualmente é: " + str(lista))
"""

# remove() = seleciona pelo VALOR  <<< 

"""
lista = ["abacate", "banana", "cenoura", "danone", "espinafre"]
print(lista)

lista.remove("danone")
print(lista)
"""

# Soma das listas - MINHA VERSÃO
c1 = [3, 4, 5, 6, 2]
c2 = [2, 3, 5, 7, 3]

c3 = []
x = 0
for i in c1:
    c3.append(c1[x] + c2[x])
    x += 1

print(c3)    

# Soma das listas - VERSÃO DO PROFESSOR
c1 = [3, 4, 5, 6, 2]
c2 = [2, 3, 5, 7, 3]

c3 = []

for i in range(0, len(c1)):
    x = c1.pop() + c2.pop()
    c3.insert(0, x) #(indice, valor)


print(c3) 

# Soma das listas - VERSÃO DO PROFESSOR COMPPLEMENTADA
c1 = [3, 4, 5, 6, 2]
c2 = [2, 3, 5, 7, 3]

c3 = []

resto = 0
for i in range(0, len(c1)):
    x = c1.pop() + c2.pop() + resto
    if (x >= 10):
        c3.insert(0, x%10)
        resto = (x - (x%10))/10
    else:
        c3.insert(0, x) #(indice, valor)
        resto = 0

print(c3) 

batata = 0

# if batata < 5:
#     batata = batata +1
#     print (batata)

# while batata > 5:
#     batata = batata +1
#     print (batata)

# print ("Fim")    

# Exemplo básico para entender WHILE:
# cont = 0
# i = 0

# while i < 5:
#     print ("Digite um número:")
#     num = int(input())
#     if num % 2 == 0:
#         cont = cont + 1
#     i = i + 1

# print ("O total de números pares são: " + str(cont))    

# Um programa para se obter médias:
print ("Deseja obter a média de quantas resultados?")
qtd_md = float(input())
nota = 0
tot = 0
resul = 0
i = 0

while i < qtd_md:
    print ("Insira o valor:")
    nota = float(input())
    tot = nota + tot
    i = i + 1

resul = (tot / qtd_md)

print("Temos como média:", resul)
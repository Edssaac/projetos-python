# Faça um programa que simule uma compra de itens em um supermercado.
# Este programa terá uma lista pré definida de itens, na forma de um dicionário e que já
# está inserido no código, este dicionário contém os nomes dos itens assim como seus
# respectivos preços.
# Você deve então permitir ao usuário inserir dois valores, o primeiro vai conter o item
# que ele deseja comprar e o segundo a quantidade; as entradas vão ser inseridas até
# que a string contendo o item seja vazia.
# Após isso, você deve retornar ao usuário o preço total de suas compras


itens = {
	"laranja" : 2.37,
	"controle" : 4.50,
	"livro" : 31.54,
	"panela" : 105.38,
	"cadeira" : 185.44,
	"TV" : 2000.00,
}

precoFinal = 0.0


# while True:
#     n = str(input("Item: "))

#     if n in itens and n != '':
#         n2 = int(input("Quantidade: "))
#         precoFinal = precoFinal + (itens[n] * n2)
#     else:
#         print(f"O preço total é: {precoFinal}")
#         break

while True:
    n = str(input("Item: ").strip())

    if n in itens:
        n2 = int(input("Quantidade: "))
        precoFinal = precoFinal + (itens[n] * n2)
    elif n == '':
        print(f"O preço total é: {precoFinal}")
        break


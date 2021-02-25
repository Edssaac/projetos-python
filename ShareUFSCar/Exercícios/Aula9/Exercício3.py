def inicializaDicionario():
	global dicionario

	while True:
		x = str(input('Palavra: '))

		if x != "": dicionario[x] = y = str(input("Significado: "))
		else: break 


def adicionaPalavra():
	global dicionario

	x = str(input("Palavra: "))
	dicionario[x] = str(input("Significado: "))

def removePalavra():
	global dicionario

	x = str(input("Palavra: "))

	del dicionario[x]


def buscaPalavra():
	global dicionario

	x = str(input("Palavra: "))

	if x in dicionario:
		return dicionario[x]
	else: return False

def printaDicionario():
	global dicionario

	print(dicionario)

############################
############################
############################


dicionario = {}


while True:
	print("Opções:",
		  "[0] Sair",
		  "[1] Inicializar o dicionário",
		  "[2] Adicionar palavra ao dicionário",
		  "[3] Retirar palavra do dicionário",
		  "[4] Buscar palavra no dicionário",
		  "[5] Printar o dicionário"
		 )

	opcao = int(input("Sua opção? "))

	if opcao == 0:
		break
	if opcao == 1:
		inicializaDicionario()
	elif opcao == 2:
		adicionaPalavra()
	elif opcao == 3:
		removePalavra()
	
	elif opcao == 4:
		significado = buscaPalavra()
		if significado == False:
			print("Está palavra não está presente no dicionário")
		else:
			print(significado)

	elif opcao == 5:
		printaDicionario()
	else:
		print("Opção inválida!")
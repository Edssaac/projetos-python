def leDados():
	file = open("contatos.txt", "r+")

	return file

def salvaDados():
	global contatos

	contatos.close()


def adicionaContato():
	global contatos

	name = str(input("Contato: "))

	ctx = contatos.read()
	contatos.writelines(name + "\n")
	ctx = contatos.read()


def removeContato():
	global contatos

	name = str(input("Contato: "))


def printaContatos():
	global contatos

	ctx = contatos.read()
	print(ctx)


############################
############################
############################

contatos = leDados()

while True:
	print("Opções:",
		  "[0] Sair",
		  "[1] Adicionar contato",
		  "[2] Remover contato",
		  "[3] Printar contatos",
		 )

	opcao = int(input("Sua opção? "))

	if opcao == 0:
		break
	elif opcao == 1:
		adicionaContato()
	elif opcao == 2:
		removeContato()
	elif opcao == 3:
		printaContatos()
	else:
		print("Opção inválida!")


salvaDados()
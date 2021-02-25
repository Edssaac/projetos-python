resquest = input("Deseja continuar? ")

if resquest == "yes" or resquest == "y" or resquest == "Yes" or resquest == "Y" or resquest == "YES":
    print ("continuando...")
    print ("Completo!")
elif resquest == "No" or resquest == "NO" or resquest == "no" or resquest == "N" or resquest == "n":
    print ("Saindo...") 
else:
    print ("Pedido Inválido.")   

# É basicamente uma escada, se o valor não passar pelo IF (se for falso para com o IF), então ele segue para o ELIF, e este se tbm for passado, chega ao final, que é o ELSE. 
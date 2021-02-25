# Arquivos


# open("file_name", "mode")
# mode:
# r = read;
# a = append; add to the original text
# w = write;
# x = crate; overwrite the original text

# file = open("texte.txt", "x") # is creating a new file
file = open("texte.txt", "w") 

# file.read(x) = returns all file contents, x is the amount of caracters. 
# print(file.read())

# lista = []
# for f in file:
#     # print(f, end="")
#     lista.append(f)

# ctx = file.read()
# print(ctx.split("\n"))


# write
lista = ["aaa", "bbb", "ccddff"]

# for f in lista:
#     file.write(f + "\n")

file.writelines(lista)


file.close() # is closing the file created or opened
# batata
# feijao
# lais
# repolho
# cafe
# saza
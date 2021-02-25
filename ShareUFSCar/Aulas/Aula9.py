# Dicionários / Dictionaries

# Diferenças entre Dicionários e Listas:
Discionario = {
    "chave1" : "valor1",
    "chave2" : "valor2",
    "chave3" : "valor3"
}
Lista = ["valor", "valor", "valor"]


# Declarando um Dicionário:
d0 = {}
#  Ou;
d1 = {
    "chave1" : "valor1",
    "chave2" : "valor2",
    "chave3" : "valor3"
}

d = {}
# Adicionando Informações (uma Chave e um Valor):
d["nova_chave"] = "novo_valor"

# Alterando Informação já existente:
d["chave_existente"] = "novo valor"
# teste = {}
# print("inicio ", teste)
# teste["batata"] = 'feijao'
# print("addendo ",teste)
# teste["batata"] = "catuaba"
# print("alt valor ", teste)


# Removendo valores (IMPOSSÍVEL REMOVER APENAS CHAVE OU VALOR, HÁ DE SER AMBOS): 
# dicionario_nome = {"chave_name" : "2"}
# print(dicionario_nome)
# del dicionario_nome["chave_name"]
# print(dicionario_nome)


# Iterando(interagindo e imprimindo):
dicionario = {
    "Chave 1" : 1,
    "Chave 2" : 2,
    "Chave 3" : 3
}
# for chave in dicionario:
#     print(chave) # "Chave 1", "Chave 2", etc
#     print(dicionario[chave]) # 1, 2, etc    

# print(dicionario["Chave 3"])


# Verificando se há determinada chave:
dicionario = {
    "Chave 1": 1
}
if "Chave 1" in dicionario: pass
# Caso a chave esteja no dicionário
else: pass
# Caso a chave não esteja no dicionário 


# Como eu descubro qual o tamanho do meu dicionário?
dicionario = {
    10 : 'AAA',
    20 : 'BBB',
    30 : 'CCC'
}
# O dicionario possui 3 chaves (10, 20 e 30)
# Para verificarmos, basta fazer a seguinte operação:
quantidade_de_chaves = len(dicionario.keys())

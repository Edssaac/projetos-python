# count = 0
# while count != 5:
#     count +=1
#     print(count)

# count = 0
# while count <= 20:
#     count += 3
#     print(count)

# count = 20
# while count >= 0:
#     count -= 3
#     print(count)

# import random
# num = random.randint(1,5)
# chute = 0
# tentativas = 0

# while (chute != num):
#     chute = input("Advinhe um número entre 1 e 5: ")
        
#     if (chute != num) == True :
#         tentativas += 1
#         continue
#     elif chute == num:
#         break
        
# print (f"Você acertou com {tentativas} tentativas!")

# import random
# num = random.randint(1,5)
# tentativas = 0
# chute = 0

# while chute != num:
#     chute = input("Digite um número: ") 
#     if chute != num:
#         print("Batatatatata")
#         print(num, chute)
#         continue
#     print("legal")

# import random

# num = random.randint(1,5)
# tentativas = 0
# chute = 0

# while chute != num:
#     tentativas += 1
#     chute = input("Adivinhe um número que está entre 1 and 5: ")
#     if chute.isnumeric():
#         chute = int(chute)
# else:
#     print(f"Você acertou com {tentativas} tentativas")         

# import random

# num = random.randint(1,5)
# tentativa = 0
# chute = 0

# print("Adivinhe um número que está entre 1 and 5:")
# while chute != num:
#     tentativa += 1
#     chute = input(f"Digite o chute #{tentativa}: ")

#     if chute.isnumeric():
#         chute = int(chute)
#     else:
#         print("Apenas números por favor!")
#         continue 

#     if chute < num:
#         print("Valor muito baixo, tente novamente!") 
#     elif chute > num:
#         print("Valor muito alto, tente novamente!")                   

# if tentativa <= 1:
#     print (f"Você acertou com {tentativa} tentativa") 
# else:
#     print (f"Você acertou com {tentativa} tentativas") 


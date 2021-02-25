# import random

# roll = 0
# count = 0

# while roll != 5:
#     count += 1
#     roll = random.randint(1,5)
#     print (roll)

# print(f"It took {count} rolls to roll a 5!")    

# import random

# roll = 0
# count = 0

# print("First person to roll a 5 wins!")
# while roll != 5:

#     name = input("Enter a name, or \"q\" to quit: ")
#     if name == "q":
#         break

#     count += 1
#     roll = random.randint(1,5)
#     print(f"{name} rolled {roll}.")

# else:
#     print(f"{name} wins!!!")    

# print (f"You rolled the dice {count} times.")

# import random

# roll = 0
# count = 0

# print ("First person to roll a 5 wins!")
# while roll != 5:
#     name = input("Enter a name, or \"q\" to quit: ")

#     if name.strip() == "": #Se não houver nada como resposta o código deve voltar para o começo.
#         continue

#     if name.strip() == "q":
#         break

#     count += 1
#     roll = random.randint(1,5)
#     print (f"{name} rolled {roll}.")

# else:
#     print(f"{name} wins!")

# print(f"You rolled the dice {count} times.")        

# import random 

# num = random.randint(1,5)
# chute = 0
# tentativa = 0

# while chute != num:
#     tentativa += 1
#     chute = input("Advinhe um núemro entre 1 e 5: ") #print(type(num), type(chute))
    
#     if chute.isnumeric():
#         chute = int(chute) #print(type(num), type(chute))
        
# else:
#     print(f"Você acertou com {tentativa} tentativas.")    

import random
num = random.randint(1,5)
chute = 0
tentativa = 0

print("Advinhe um número entre 1 e 10!")

while chute != num:
    tentativa += 1
    chute = input(f"Tentativa #{tentativa}: ")

    if chute.isnumeric():
        chute = int(chute)

    else:
        print("Apenas números, por favor!")  
        continue

    if chute < num:
        print("Muito baixo, tente novamente!")
    if chute > num:
        print("Muito alto, tente novamente!")        

else:
    print(f"Você acertou com {tentativa} tentativas!")    
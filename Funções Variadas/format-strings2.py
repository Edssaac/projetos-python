# message = str.capitalize('first message')
# print(message)

# message = 'second message'.capitalize()
# print(message)

# message = 'third message'
# print(message.capitalize())

# a = "batata"
# b = "feijao"
# print (a.capitalize(), b.capitalize())

# message = 'hello world'
# print(message.lower())
# print(message.upper())
# message = message.title()
# print(message)
# print(message.swapcase())

# a = "batata feijao"
# print (a.title())

# location = 'Mississippi'
# print(location.count('s'))

# a = "batata feijao"
# print (a.count("t"))

# a = input("Deseja casar comigo? ")
# if a.count("sim") == True:
#     print("Casado")
# elif a.count("nao") == True:
#     print("Não casado") 
# else:
#     print("ulalah") 

# print(len('how many letters in this string?'))     

# message = 'racecar'
# print(message.startswith('r'))
# print(message.startswith('a'))
# print(message.startswith('ra'))

# print(message.endswith('r'))
# print(message.endswith('a'))
# print(message.endswith('ar'))

# message = 'The quick brown fox jumps over the lazy dog'
# print(message.find('q'))

# print(message.find('t'))
# print(message.find('T'))

# message = '    mid  dle     '
# print('.' + message.lstrip() + '.')
# print('.' + message.rstrip() + '.')
# print('.' + message.strip() + '.')

# message = 'brevity is the essence of wit'
# message = message.replace('essence', 'soul')
# print(message)

# confissão = "eu sou gay"
# print (confissão.replace("gay", "hétero")) 

# message = 'howdy'
# print(message.rjust(20))
# print(message.rjust(20, '-'))
# print(message.ljust(20))
# print(message.ljust(20, '-'))

a = "batata"
print (a.rjust(30, "k") + " gay".ljust(10, ".") + "a")
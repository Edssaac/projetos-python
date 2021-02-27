# Conversão Entre Bases Númericas

try:
    convbase = str(input())
    if convbase != "BD" and convbase != "DB": raise ValueError

    num = int(input())

    if convbase == "BD":
        print(int(str(num), 2))
    elif convbase == "DB":
        print(bin(num)[2:])
except ValueError: print("Houve algum erro, tente novamente!")
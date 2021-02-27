# Calculadora Avançada
from math import sqrt

MSG_ERRO = 'Operação inválida!'

def is_float(value):
    x = 0
    try:
        x = float(value)
    except:
        return False
    return True

def get_index(operand):
    return int(operand[1:]) - 1


memoria = []
while True:
    values = input().split()
    v1 = None
    v2 = None

    if values[0] in ("m", "M"):
        try:
            memoria.append(soma)
            # print(memoria)
            continue
        except NameError: print(MSG_ERRO); continue

    try:
        if values[0] == "#":

            if values[1][0] in ("m", "M"):
                try: 
                    v1 = memoria[ get_index( values[1] ) ]
                    print(sqrt(v1))
                except IndexError: print(MSG_ERRO); continue

            else: print(sqrt(int(values[1])))

        else:
            if values[0] in ("q", "Q"):
                break
            else:

                if len(values) < 3: print(MSG_ERRO);continue


                try:
                    if is_float(values[0]): v1 = float(values[0])
                    else: v1 = int(values[0])

                    if is_float(values[2]): v2 = float(values[2])
                    else: v2 = int(values[2])
                except:
                    if values[0][0] in ("m", "M"):
                        try: 
                            v1 = memoria[ get_index( values[0] ) ]
                        except IndexError: print(MSG_ERRO); continue

                    if values[2][0] in ("m", "M"):
                        try: 
                            v2 = memoria[ get_index( values[2] ) ]
                        except IndexError: print(MSG_ERRO); continue

                try:
                    if values[1] == "+":
                        soma = v1 + v2

                    elif values[1] == "-":
                        soma = v1 - v2

                    elif values[1] == "*":
                        soma = v1 * v2

                    elif values[1] == "/":
                        if 0 in (v1, v2):
                            # print("Divisão por zero") 
                            print(MSG_ERRO) 
                            continue
                        else: soma = v1 / v2

                    elif values[1] == "^":
                        soma = v1 ** v2

                    print(soma)
                except: print(MSG_ERRO); continue
    except ValueError:
        # print("Sintaxe inválida")
        print(MSG_ERRO)
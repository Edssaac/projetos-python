# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Versão do Professor:
# entrada = [int(i) for i in input().split()]

# hora_inicial = entrada[0]
# minuto_inicial = entrada[1]
# hora_final = entrada[2]
# minuto_final = entrada[3]

# hora_total = hora_final - hora_inicial

# if hora_total < 0:
#     hora_total += 24

# minuto_total = minuto_final - minuto_inicial

# if minuto_total < 0:
#     minuto_total += 60
#     hora_total -= 1

# if hora_total == 0 and minuto_total == 0:
#     print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
# else:
    # print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora_total, hora_inicial))    



# Minha versão:
print("- Quanto tempo passou? -")

hora_inicial = int(input("Hora Inical: "))
minuto_inicial = int(input("Minuto Inicial: "))
hora_final = int(input("Hora Final: "))
minuto_final = int(input("Minuto Final: "))

hora_total = hora_final - hora_inicial
minuto_total = minuto_final - minuto_inicial

if (hora_total < 0):
    hora_total += 24

if (minuto_total < 0):
    minuto_total += 60
    hora_total -= 1

if (hora_total == 0 and minuto_total == 0):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")  
else:
    print(f"O JOGO DUROU {hora_total} HORA(S) E {minuto_total} MINUTO(S)") 
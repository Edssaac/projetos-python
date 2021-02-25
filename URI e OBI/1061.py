# Pedrinho está organizando um evento em sua Universidade. O evento deverá ser no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho quer calcular o tempo que o evento vai durar, uma vez que ele sabe quando inicia e quando termina o evento.

# Sabendo que o evento pode durar de poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração deste evento.

# dia = int(input("Dia: "))
# hh, mm, ss = map(int, input().split())

# diaF = int(input("Dia: "))
# hhF, mmF, ssF = map(int, input().split())

# W = diaF - dia
# X = hhF - hh
# Y = mmF - mm
# Z = ssF - ss

# if (X < 0):
#     X += 24
#     W -= 1

# print(f"{W} dia(s)\n{X} hora(s)\n{Y} minuto(s)\n{Z} segundo(s)")



# Versão do Professor:
dia_inicial = int(input().split()[1])

hora = input().split(":")
hora_inicial = int(hora[0])
minuto_inicial = int(hora[1])
segundo_inicial = int(hora[2])

dia_final = int(input().split()[1])

hora = input().split(":")
hora_final = int(hora[0])
minuto_final = int(hora[1])
segundo_final = int(hora[2])

dias = dia_final - dia_inicial

horas = hora_final - hora_inicial

if horas < 0:
    horas += 24
    dias -= 1

minutos = minuto_final - minuto_inicial

if minutos < 0:
    minutos += 60
    horas -= 1

segundos = segundo_inicial - segundo_final

if segundos < 0:
    segundos += 60
    minutos -= 1

print("{} dia(s)".format(dias))    
print("{} hora(s)".format(horas))    
print("{} minuto(s)".format(minutos))    
print("{} segundo(s)".format(segundos))    
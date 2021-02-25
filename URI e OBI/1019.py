# Conversão de Tempos

# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

N = int(input())

hh = mm = ss = 0 

while N > 0:
    if N > 0:
        ss += 1
        N -= 1
    if ss >= 60:
        mm += 1
        ss = 0
    if mm >= 60:
        hh += 1
        mm = 0

print("{}:{}:{}".format(hh, mm, ss))
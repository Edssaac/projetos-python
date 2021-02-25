import math
listaA = [36, 484, 25]
listaB = [5, 6, 22]

d = {}

for i in listaA:
    d[i] = int(math.sqrt(i))

print(d)


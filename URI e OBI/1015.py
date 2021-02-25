# Distância Entre Dois Pontos

# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:
# Distancia = √(x2 - x1)² + (y2 - y1)² 

import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

t = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
t = math.sqrt(t)

print("%.4f"%t)
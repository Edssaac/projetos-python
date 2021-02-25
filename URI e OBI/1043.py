# Triângulo

# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

# Perimetro = XX.X

# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

# Area = XX.

A, B, C = map(float, input().split())

if ( (A < B + C) and (B < A + C) and (C < A + B) ):
    p = (A + B + C)
    print("Perimetro = {}".format(p))
else:
    area = ((A + B) / 2) * C

    print("Area = {}".format(area))
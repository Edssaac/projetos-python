valores = list( map(float, input().split()))

while not (valores[0] == valores[1] == valores[2] == 0.0):
    # i = H × 100 ÷ C
    i = valores[0] * 100 / valores[1]

    if i <= 8.334 and valores[2] > 0.7:
        print("PROJETO SIMPLES")
    else: 
        print("PROJETO ESPECIAL")

    valores = list( map(float, input().split()))








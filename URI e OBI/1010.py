# Cálculo Simples

# Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

cdgp, qtdp, vp = input().split()
cdgp2, qtdp2, vp2 = input().split()

cdgp, qtdp, vp, cdgp2, qtdp2, vp2 = [int(cdgp), int(qtdp), float(vp), int(cdgp2), int(qtdp2), float(vp2)]

t = (qtdp * vp) + (qtdp2 * vp2)

print("VALOR A PAGAR: R$ {}".format("%0.2f"%t))
# Idade em Dias

# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

x = int(input())

aa = int(x / 365)
y = int(x - (aa * 365))
mm = int(y / 30)
dd = int(y - (mm * 30))

print("{} ano(s)".format(aa))
print("{} mes(es)".format(mm))
print("{} dia(s)".format(dd))
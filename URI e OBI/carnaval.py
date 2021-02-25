# Lê valores para uma lista, separa em espaços, e limita a cinco valores;
notas = list(map(float, input().split()[:5]))
# Deixa a lista em ordem crescente;
notas.sort()
# Imprime a soma das notas do meio, de forma que o numero de casas depois da vírgula seja 1.
print("{:.1f}".format( (notas[1]+notas[2]+notas[3])))
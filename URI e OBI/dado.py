jogadas = int(input())
sequencia_numeros = list(map(int, input().split()[:jogadas]))

luisa, antonio = 0, 0

jogador_atual = "luisa"
for i in sequencia_numeros:

    if jogador_atual == "luisa":
        luisa += i
    else:
        antonio += i

    if i != 6:
        if jogador_atual == "luisa":
            jogador_atual = "antonio"
        else:
            jogador_atual = "luisa"

if luisa == antonio:
    print(f"EMPATE {luisa}\n")
elif luisa > antonio:
    print(f"LUISA {luisa}\n")
else:
    print(f"ANTONIO {antonio}\n")
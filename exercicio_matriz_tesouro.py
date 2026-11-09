import random

def caca_tesouro():
    mapa = []
    for i in range(5):
        mapa.append([".", ".", ".", ".", "."])

    tesouro_linha = random.randint(0, 4)
    tesouro_coluna = random.randint(0, 4)
    tentativas = 0

    print("=== CAÇA AO TESOURO ===")
    while True:
        print("\n    0 1 2 3 4")
        for i in range(5):
            print(i, "|", " ".join(mapa[i]))

        try:
            linha = int(input("Linha (0 a 4): "))
            coluna = int(input("Coluna (0 a 4): "))
        except ValueError:
            print("Digite apenas números inteiros!")
            continue

        if linha < 0 or linha > 4 or coluna < 0 or coluna > 4:
            print("Posição fora do mapa!")
            continue

        tentativas += 1
        distancia = abs(linha - tesouro_linha) + abs(coluna - tesouro_coluna)

        if distancia == 0:
            break
        mapa[linha][coluna] = "X"
        if distancia == 1:
            print("Dica: Muito perto!")
        elif distancia <= 3:
            print("Dica: Perto.")
        else:
            print("Dica: Longe.")

    mapa[tesouro_linha][tesouro_coluna] = "T"
    print("\n    0 1 2 3 4")
    for i in range(5):
        print(i, "|", " ".join(mapa[i]))
    print(f"Parabéns! Você encontrou o tesouro em ({tesouro_linha}, {tesouro_coluna})!")
    print(f"Número de tentativas: {tentativas}")

if __name__ == "__main__":
    caca_tesouro()

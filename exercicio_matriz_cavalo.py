
def tabuleiro_cavalo():
    # Movimento do cavalo em um tabuleiro 8x8

    # 1) Cria o tabuleiro 8x8 com "." em todas as casas
    tabuleiro = []
    for i in range(8):
        linha_do_tabuleiro = []
        for j in range(8):
            linha_do_tabuleiro.append(".")
        tabuleiro.append(linha_do_tabuleiro)

    # 2) Pede a posição do cavalo (de 0 a 7)
    linha = int(input("Digite a linha do cavalo (0 a 7): "))
    coluna = int(input("Digite a coluna do cavalo (0 a 7): "))

    # Repete até o usuário digitar uma posição dentro do tabuleiro
    while linha < 0 or linha > 7 or coluna < 0 or coluna > 7:
        print("Posição inválida! Use números de 0 a 7.")
        linha = int(input("Digite a linha do cavalo (0 a 7): "))
        coluna = int(input("Digite a coluna do cavalo (0 a 7): "))

    # 3) Os 8 movimentos em "L" do cavalo: [quanto muda a linha, quanto muda a coluna]
    movimentos = [
        [-2, -1], [-2, 1],
        [-1, -2], [-1, 2],
        [1, -2], [1, 2],
        [2, -1], [2, 1],
    ]

    # 4) Testa cada movimento e marca com "*" se cair dentro do tabuleiro
    total = 0
    for passos in movimentos:
        nova_linha = linha + passos[0]
        nova_coluna = coluna + passos[1]

        if nova_linha >= 0 and nova_linha <= 7 and nova_coluna >= 0 and nova_coluna <= 7:
            tabuleiro[nova_linha][nova_coluna] = "*"
            total = total + 1

    # 5) Coloca o cavalo no tabuleiro
    tabuleiro[linha][coluna] = "C"

    # 6) Mostra o tabuleiro
    print()
    for i in range(8):
        for j in range(8):
            print(tabuleiro[i][j], end=" ")
        print()

    print()
    print("Posição do cavalo: linha", linha, "e coluna", coluna)
    print("Movimentos possíveis:", total)

if __name__ == "__main__":
    tabuleiro_cavalo()

tabuleiro = [
    [" ", " ", " "],  # Linha 0
    [" ", " ", " "],  # Linha 1
    [" ", " ", " "]   # Linha 2
]

def print_board(bord):
    for linha in bord:
        print(f"| {linha[0]} | {linha[1]} | {linha[2]} |")
        print()

def jogada(jogador):

    if jogador == "X":
        number = 1
    elif jogador == "O":
        number = 2

    print(f"Sua vez, jogador {number}")

    choice = int(input("Diga sua jogada (1-9): ").strip())

    linha = (choice -1) // 3
    coluna = (choice -1) % 3

    #verifica se está vazio
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
    else:
        print()
        print("Esse espaço já está preenchido!")




while True:
    print_board(tabuleiro)
    jogada("X")
    print_board(tabuleiro)
    jogada("O")

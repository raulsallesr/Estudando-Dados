tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
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

    while True:
        try:
            choice = int(input("Diga sua jogada (1-9): ").strip())
            if choice < 1 or choice > 9:
                print("Escolha inválida! Escolha um número de 1 a 9.")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número.")
            continue

        linha = (choice - 1) // 3
        coluna = (choice - 1) % 3

        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            break
        else:
            print("Esse espaço já está preenchido! Escolha outro.")

def checar_vitoria(tabuleiro):
    # Linhas
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != " ":
            return tabuleiro[linha][0]

    # Colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != " ":
            return tabuleiro[0][coluna]

    # Diagonal principal
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        return tabuleiro[0][0]

    # Diagonal secundária
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        return tabuleiro[0][2]

    return None

def checar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

while True:
    print_board(tabuleiro)
    jogada("X")
    vencedor = checar_vitoria(tabuleiro)
    if vencedor:
        print_board(tabuleiro)
        print(f"Jogador {vencedor} venceu!")
        break
    if checar_empate(tabuleiro):
        print_board(tabuleiro)
        print("Empate!")
        break

    print_board(tabuleiro)
    jogada("O")
    vencedor = checar_vitoria(tabuleiro)
    if vencedor:
        print_board(tabuleiro)
        print(f"Jogador {vencedor} venceu!")
        break
    if checar_empate(tabuleiro):
        print_board(tabuleiro)
        print("Empate!")
        break

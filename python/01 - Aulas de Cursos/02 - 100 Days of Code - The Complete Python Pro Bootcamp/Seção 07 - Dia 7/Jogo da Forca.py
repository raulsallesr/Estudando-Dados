import random

# Palavras possíveis
lista_palavras = ["PALMEIRAS", "MAX", "RELOGIO", "TELEVISAO", "PYTHON", "DADOS"]

# Bonequinhos da forca (vai desenhando a cada erro)
stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

# 1 - escolher palavra aleatória
chosen_word = random.choice(lista_palavras)
size_word = len(chosen_word)

# 2 - variáveis de controle
letras_corretas = []
letras_erradas = []
tentativas = 6   # 6 chances antes de perder
gameover = False

print("🎮 Bem-vindo ao jogo da Forca!\n")
print("_ " * size_word)  # placeholder inicial

# 3 - loop do jogo
while not gameover:
    guess = input("Chute uma letra: ").upper()

    display = ""
    for letter in chosen_word:
        if letter in letras_corretas or letter == guess:
            display += letter
        else:
            display += "_"

    # atualizar letras corretas
    if guess in chosen_word:
        if guess not in letras_corretas:
            letras_corretas.append(guess)
    else:
        if guess not in letras_erradas:
            letras_erradas.append(guess)
            tentativas -= 1
            print(f"❌ Errou! Você ainda tem {tentativas} tentativas.")

    # mostrar progresso
    print(stages[6 - tentativas])  # mostra bonequinho
    print("Palavra: " + " ".join(display))
    print("Letras certas: ", letras_corretas)
    print("Letras erradas: ", letras_erradas)

    # condição de vitória
    if "_" not in display:
        gameover = True
        print("🎉 Você venceu! A palavra era:", chosen_word)

    # condição de derrota
    if tentativas == 0:
        gameover = True
        print("💀 Você perdeu! A palavra era:", chosen_word)

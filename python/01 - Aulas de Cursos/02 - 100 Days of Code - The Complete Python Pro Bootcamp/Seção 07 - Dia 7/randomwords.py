lista_palavras = ["PALMEIRAS", "MAX", "RELOGIO", "TV"]

# 1 - escolher uma palavra aleatória

# 2 - pedir p jogador acertar uma letra    

# 3 - checar se a letra é certa ou não
import random
escolher_palavra = random.choice(lista_palavras)
tamanho_palavra = len(escolher_palavra)
palavra_em_letras = list(escolher_palavra)

print(escolher_palavra)


while tamanho_palavra > 0:
    adivinhar = input("Fala uma letra: ").upper().strip()
    if adivinhar in palavra_em_letras:
        print("acertou")
    elif adivinhar not in palavra_em_letras:
        print("Errouuu")
        tamanho_palavra -= 1
        if tamanho_palavra > 0:
            print(f"Você tem mais {tamanho_palavra} vidas!")
        else:
            print("Game over")
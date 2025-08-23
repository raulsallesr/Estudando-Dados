lista_palavras = ["PALMEIRAS", "MAX", "RELOGIO", "TV"]

# 1 - escolher uma palavra aleatória

# 2 - pedir p jogador acertar uma letra    

# 3 - checar se a letra é certa ou não
import random
chosen_word = random.choice(lista_palavras)
print(chosen_word)
size_word = len(chosen_word)
placeholder = ""

for x in range(0,size_word):
    placeholder += "_"
print(placeholder)


while display != chosen_word:
    guess = input("Chute uma letra: ").upper()

    display= ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"
    print(display)
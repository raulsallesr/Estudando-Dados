# pegar frase do usuário
original = input("Diga uma frase: ").strip().lower()

# separar em palavras
words = original.split() #.split separa em palavras!

# loop por cada letra e converter em pig latin

new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
print(new_words)


# se começar com vogal, adicionar "yay" no final
# se não, mover a primeira consoante p final e adicionar "ay"

# mudar ordem de letras

# print final
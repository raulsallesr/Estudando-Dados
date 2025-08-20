letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

print("Bem vindos ao gerador de senha 2000!")

qtd_letras = int(input("Quantas letras você vai querer na senha?: "))
qtd_numeros = int(input("Quantos numeros você vai querer na senha?: "))
qtd_simbolos = int(input("Quantos simbolos letras você vai querer na senha?: "))

senha = []

for x in range(0, qtd_letras):
    senha.append(random.choice(letters))

for x in range(0, qtd_numeros):
    senha.append(random.choice(numbers))

for x in range(0, qtd_simbolos):
    senha.append(random.choice(symbols))


random.shuffle(senha)
senha_junta = "".join(senha)

print(senha_junta)

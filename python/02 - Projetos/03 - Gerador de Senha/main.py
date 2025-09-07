# vamos criar um gerador de senha simples
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

print("Bem vindo.")

qtd_letras = int(input("Quantas letras você quer na senha? "))
qtd_numeros = int(input("Quantos numeros você quer na senha? "))
qtd_simbolos = int(input("Quantos simbolos você quer na senha? "))

print(qtd_letras, qtd_numeros, qtd_simbolos)


senha = []

for x in range(0, qtd_letras):
    senha.append(random.choice(letters))

for x in range(0, qtd_numeros):
    senha.append(random.choice(numbers))

for x in range(0, qtd_simbolos):
    senha.append(random.choice(symbols))

print(senha)

random.shuffle(senha)

senha_final = ""
for x in senha:
    senha_final += x

print(senha_final)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

print("Bem vindos ao gerador de senha 2000!")

qtd_letras = int(input("Quantas letras você vai querer na senha?: "))
qtd_numeros = int(input("Quantos numeros você vai querer na senha?: "))
qtd_simbolos = int(input("Quantos simbolos letras você vai querer na senha?: "))

escolha_letras = random.choices(letters, k=qtd_letras)
escolha_numeros = random.choices(numbers, k=qtd_numeros)
escolha_simbolos = random.choices(symbols, k=qtd_simbolos)

senha_lista = escolha_letras + escolha_numeros + escolha_simbolos

random.shuffle(senha_lista)

senha_final = "".join(senha_lista)

print(f"Sua senha final é: {senha_final}")

# agora o nivel hard kk

print("Bem vindos ao gerador de senha 2000!")

qtd_letras = int(input("Quantas letras você vai querer na senha?: "))
qtd_numeros = int(input("Quantos numeros você vai querer na senha?: "))
qtd_simbolos = int(input("Quantos simbolos letras você vai querer na senha?: "))

lista_senha = []

for i in range(0, qtd_letras):
    lista_senha.append(random.choice(letters))

for i in range(0, qtd_numeros):
    lista_senha.append(random.choice(numbers))

for i in range(0, qtd_simbolos):
    lista_senha.append(random.choice(symbols))


random.shuffle(lista_senha)

senha = ""
for x in lista_senha:
    senha += x

print(senha)

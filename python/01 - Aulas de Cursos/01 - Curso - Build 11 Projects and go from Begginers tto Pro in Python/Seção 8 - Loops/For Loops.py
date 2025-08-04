# for VARIAVEL in RANGE pode ser uma lista
# a variavel é atualizada toda vez pelo loop
for number in range (1,3): # se colocar (1,3,2) -- o último quer dizer que vamos de 2 em 2
    print(number)

for letter in "abcd":
    print(letter)


# p pegar vogais e consoantes
vogais = 0
consoantes = 0

frase = "Vai palmeirasss porra"
for letras in frase:
    if letras.lower() in "aeiou":
        vogais = vogais + 1
    elif letter == " ":
        pass
    else:
        consoantes = consoantes +1
print(f'Temos {vogais} vogais e {consoantes} consoantes na frase "{frase}"')


estudantes = {
    "Homens": ["Raul", "Max", "Tom"],
    "Mulheres": ["Maria", "Sara", "Bruna"]
}

# print(key) # Vai retornar "Homens" e "Mulheres"
# print(estudantes[key]) # Retorna os nomes


for key in estudantes.keys():
    for name in estudantes[key]:
        if "a" in name:
            print(name)


# escrevendo solo:

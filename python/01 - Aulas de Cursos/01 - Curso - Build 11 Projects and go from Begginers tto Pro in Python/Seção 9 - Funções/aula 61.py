# nome da aula é pack and unpacking kkkkk 
# print(*variavel)

numeros = [1,2,3,4,5]
print(numeros)
print(*numeros)

frase = "Olá"
print(*frase)


def soma(*numeros_inteiros):
    total = 0
    for number in numeros_inteiros:
        total += number
    return total

print(soma(1,2,3,4,99))









# * = sem nome // numeros
# ** = com nome // dicionario



def adivinhar_tudo(**x):
    for key, value in x.items():
        print(f"{key}: {value}")

adivinhar_tudo( raul = "Boleiro", messi = "Padeiro", RMarques = "Goleador")



def zao(**x):
    for chave, valor in x.items():
        print(f"{valor}zão!")
zao(comida = "Leite", cor = "Verde", movel = "Mesa")
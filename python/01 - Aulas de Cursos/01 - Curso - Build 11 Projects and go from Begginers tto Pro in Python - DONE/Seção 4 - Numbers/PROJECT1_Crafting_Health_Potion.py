import random as rd # aqui vamos importar esse módulo, para criar um numero aleatório

start_health = 50 # Criando a variavel de vida, com valor de 50

difficulty = 1

# auqi vamos criar a variavle de poção de vida, chamando o módulo random, com o range de 25 a 50
# Tudo dentro de int(), para não criarmos um float, e sempre usar inteiros
potion_health = int(rd.randint(25,50) / difficulty) # Vamos dividir pela dificuldade tmb

new_health = start_health + potion_health

print(start_health, potion_health, new_health)

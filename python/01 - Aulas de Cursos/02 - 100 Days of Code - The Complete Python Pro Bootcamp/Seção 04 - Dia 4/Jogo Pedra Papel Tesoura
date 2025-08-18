# jogo de pedra papel tesoura
import random

print("Bem vindo ao jogo da vida, pedra papel e tesoura valendo facada")

opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

jogador = int(input("Escolha 1 para Pedra, 2 para Papel ou 3 para tesoura"))
computador = random.randint(1, 3)

print(f"Você escolheu: {opcoes[jogador]}")
print(f"O computador escolheu: {opcoes[computador]}")

# Regras simples
if jogador == computador:
    print("Empate!")
elif jogador == 1 and computador == 3:
    print("Você venceu! Pedra quebra Tesoura")
elif jogador == 2 and computador == 1:
    print("Você venceu! Papel embrulha Pedra")
elif jogador == 3 and computador == 2:
    print("Você venceu! Tesoura corta Papel")
else:
    print("Você perdeu!")

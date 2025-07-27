## // é para dividir e nao virar float
# % é para ver quanto sobra da divisão
# Vamos usar () para definir oq vai ser realizado primeiro


usando_divisao = 10/3
usando_duasbarrar = 10//3

print(usando_divisao)
print(usando_duasbarrar)
      
"""
 Ordem dos sinais:
    Brackets ()
    Order
    Division
    Multiplication
    Addition
    Subtraction

"""

# usamos o ROUND para arredondar -- a partir de .5 vai p cima
print(round(1.1))
print(round(1.5))

# COnseguimos usar a biblioteca MATH p manipular isso tmb
import math

print(math.floor(3.8)) # floor força para baixo
print(math.ceil(4.2)) # ceil força para o teto

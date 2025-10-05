"""
FOR Variável IN o_que_será_iterado:
Oq pode ser iterado:
range, list, enumerate...
"""

lista_a = ['oi', 33, 321, "Palmeiras", 5]

"""for i in range(len(lista_a)):
    print(i)
"""

# Essa é mais bonita de se fazer
for i in enumerate(lista_a):
    print(i)

    
""" 3.4 Exercício 1 - 
Crie um condicional que, dada uma variável, faça as operações:
- Se for número positivo, retorna "Número positivo"
- Se for número negativo, retorna "Número negativo"
- Se for zero, retorna "zero"
- Se não for número, retorna "Não é um número"
"""

numero = int(input("qual o numero?: "))

if numero > 0:
    print("O número é positivo")
elif numero < 0: 
    print("O Número é negativo")
elif numero == 0:
    print("0")
else:
    "Não é número"


""" 3.5 Exercício 2 - 
Faça um loop **for** para criar uma lista que intercale os valores das listas a seguir:
- valores = [1,2,3,4,5] 
- letras = ['a','b','c','d','e']

Dica: você pode utilizar o método .append() que adiciona um elemento ao final da lista."""

valores = [1,2,3,4,5] 
letras = ['a','b','c','d','e']

for x in enumerate(valores, letras)
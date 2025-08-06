"""from  random import choice

question = ["Por que o céu é azul?: ", 
            "Por que a gente nao voa?: ", 
            "Por que oa aliens não vem?: "
            ]

question = choice(question)
answer = input(question).strip().title()

while answer != "Just Because":
    answer = input("Why?: ").strip().title()


print("Ok...")
"""

# tentando escrever sozin agora:

from random import choice

perguntas = ["Pq nascemos no Brasil? ", "Por que a agua é transparente? ", "Oq é bluetooth? "]

perguntas = choice(perguntas)
resposta = input(perguntas).strip().lower()

while resposta != "pq sim":
    resposta = input("Mas pq?? ").strip().lower()

print("ok então...")

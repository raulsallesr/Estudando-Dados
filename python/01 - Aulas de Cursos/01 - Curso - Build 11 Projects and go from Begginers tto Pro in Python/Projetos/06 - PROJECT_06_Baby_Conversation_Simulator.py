from  random import choice

question = ["Por que o céu é azul?: ", 
            "Por que a gente nao voa?: ", 
            "Por que oa aliens não vem?: "
            ]

question = choice(question)
answer = input(question).strip().title()

while answer != "Just Because":
    answer = input("Why?: ").strip().title()


print("Ok...")
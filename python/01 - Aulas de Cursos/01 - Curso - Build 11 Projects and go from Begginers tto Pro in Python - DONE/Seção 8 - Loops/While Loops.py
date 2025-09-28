"""number = 1

while number <= 24:
    print(number)
    number = number + 1
"""    

names = []

while len(names) < 3:
    nome = input("Por favor, me diga um nome: ").strip().title()
    names.append(nome)

print("Lista cheia")
print(names)

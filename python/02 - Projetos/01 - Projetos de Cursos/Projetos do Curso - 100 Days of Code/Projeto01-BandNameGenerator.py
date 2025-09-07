# Criar um gerador de nome de banda, pedindo ao usuário qual cidade ele nasceu e o nome do pet

print("Welcome to the Band Name Generator :)")
city = input("Qual o nome da cidade que você nasceu? \n").strip()
pet = input("Qual o nome do seu pet?: \n").strip()

print(f"O nome da sua banda poderia ser {city} {pet}")

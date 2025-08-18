frutas = {"Maça", "Abacate", "Manga rs"}

for x in frutas:
    print(x)
    print("Gosto muitoooooo")



notas = [11, 321, 432, 12, 52, 542, 73, 12, 532, 1, 4, 8, 86, 85, 87, 45, 56, 34, 74]

#total = sum(notas)
#print(total)

#total_for = 0
#for nota in notas:
#    total_for += nota
# print(total_for)

# Desafio: replicar isso de cima para função MAX()
maximo = max(notas)
print(maximo)

maior_nota = 0
for nota in notas:
    if maior_nota < nota:
        maior_nota = nota
print(maior_nota)

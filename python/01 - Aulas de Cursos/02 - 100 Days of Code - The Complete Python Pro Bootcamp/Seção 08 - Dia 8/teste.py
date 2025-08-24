

def calculate_love_score(nome1, nome2):
    contagem1 = 0
    contagem2 = 0
    for letter in nome1:
        if letter in "true":
            contagem1 += 1
    for letter in nome2:
        if letter in "true":
            contagem2 += 1
    print(contagem1)
    print(contagem2)
    

calculate_love_score(nome1 = "Raul", nome2 = "Bruna")
cinema = {
    "Interstelar": [16, 4],
    "Piratas do Caribe": [18, 3],
    "Formula 1": [14,  5],
    "Efeito Borboleta" :[21, 7]
}

print("Olá, eu sou o Guardião do Sistema de Cinema, vamos começar :)")

while True:
    escolha_filme = input("Qual filme você deseja ver hoje? ").strip().title() # Title é p primeiras palavras virem em maiusculo
    
    if escolha_filme in cinema:
        age = int(input("Qual sua idade? "))

        if age >= cinema[escolha_filme][0]:

            num_poltronas = cinema[escolha_filme][1]

            if num_poltronas > 0:
                print("Curta o filme")
                cinema[escolha_filme][1] = cinema[escolha_filme][1] -1

            else:
                print("Desculpe, estamos cheios!")
        else:
            print("Você é muito novo para esse filme...")
    else: 
        print("Não temos esse filme!")
        
    print(f"Lista de filmes disponíveis: {cinema}")

    continuar = input("\nDeseja escolher outro filme? (y/n): ").strip().lower()
    if continuar != "y":
        print("Até mais")
        break


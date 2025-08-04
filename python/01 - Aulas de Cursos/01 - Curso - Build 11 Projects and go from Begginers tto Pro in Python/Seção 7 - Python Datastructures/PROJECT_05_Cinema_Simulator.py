cinema = {
    "Filme 1": {"Nome do Filme": "Interstelar", "Idade Mínima": 16, "Poltronas": 4},
    "Filme 2": {"Nome do Filme": "Piratas do Caribe", "Idade Mínima": 18, "Poltronas": 3},
    "Filme 3": {"Nome do Filme": "Formula 1", "Idade Mínima": 14, "Poltronas": 5},
    "Filme 4": {"Nome do Filme": "Efeito Borboleta", "Idade Mínima": 21, "Poltronas": 7}
}

print("Olá, eu sou o Guardião do Sistema de Cinema, vamos começar :)")

while True:
    escolha_filme = input("Qual filme você deseja ver hoje? ").strip().title() # Title é p primeiras palavras virem em maiusculo
    
    if escolha_filme in cinema[1]:
        age = int(input("Qual sua idade? "))

        if age >= cinema[escolha_filme]["Idade Mínima"]:

            num_poltronas = cinema[escolha_filme[2]]:

            if num_poltronas > 0:
                print("Curta o filme")
                cinema[escolha_filme][2] = cinema[escolha_filme][2] -1

            print("vc pode ver")        
        else:
            print("Você é muito novo para esse filme...")
    else: 
        print("Não temos esse filme!")



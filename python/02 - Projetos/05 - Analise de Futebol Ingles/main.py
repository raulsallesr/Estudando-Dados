with open("02 - Projetos/05 - Analise de Futebol Ingles/1-premierleague.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

for l in linhas[:20]:
    print(l.strip())

    
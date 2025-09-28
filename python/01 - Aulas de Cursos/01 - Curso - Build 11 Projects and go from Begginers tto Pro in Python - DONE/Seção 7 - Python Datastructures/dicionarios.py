# Dicionario é uma lista com varios valores, ligados a uma "key word"
estudantes = {"Raul": 24, "Bruna": 25, "Max": 10}
print(estudantes)

#Para adicionar algo, só colocar estudantes["Key word"] = xx
estudantes["Caju"] = 2
print(estudantes)

#Para ver as keys do dicionario = estudantes.keys()
print(estudantes.keys())

# ou p pegar os valores = estudantes.values()
print(estudantes.values())

# p usar o index, vamos colocar o dicionario numa varivel
a = list(estudantes)
print(a[2]) # p ver o mamax :)

# Próximo nivel de dicionário, vamos colocar multiplos valores dentro de cada chave
jogadores = {
    "Dudu": {"id": "ID001", "age": 7, "nota":"A"},
    "Rafael Marques": {"id": "ID002", "age": 10, "nota": "S"},
    "Barcos": {"id": "ID003", "age": 9, "nota": "A"}
}
print(jogadores)
print(jogadores["Dudu"])
print(jogadores["Barcos"]["nota"])
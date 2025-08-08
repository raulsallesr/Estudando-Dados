def about(nome, idade, gosto="Futebol"): # futebol  já está no parâmetro
    frase = f"Conheça o {nome}, o cara é pika, ele tem {idade} anos, e gosta de {gosto}, kkk malucao demais"
    return frase

print(about("Raul", 24, "Palmeiras"))
print(about(nome="Samuel", idade= 33, gosto="morar no Canadá"))

print(about(nome = "Messi", idade= 40))


# criar uma com alguns default já:
def descricao(altura = 1.80, idade = 24, sexo = "Masculino"):
    frase = f"Eu tenho {altura}, {idade} anos e sou do sexo {sexo}"
    return frase

print(descricao(altura= 181))
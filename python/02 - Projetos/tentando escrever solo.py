# primeiro vamos setar as taxas
# depois vamos pedir um valor # dar a chance do cara sair kkk
# testar se o valor numero mesmo
# perguntar qual moeda destino
# setar qual taxa ele escolheu
# testar se temos a taxa
# converter o valor
# printar o valor

taxas = {
    "usd": 5.5,
    "dolar": 5.5,
    "euro": 5.7,
    "pesos": 0.3
}

while True:
    #pegar o valor
    valor = input("Digite um valor ou sair para sair :) ")

    # checar se ele quer sair
    if valor.lower() == "sair":
        print("ok... adeus")
        exit()
    
    # checar se é numero

    try:
        valor = float(valor)
    except ValueError:
        print("É para digitar um numero!!!")
        continue

    moeda_destino = input("Qual a moeda destino?: ").strip().lower()

    taxa = taxas.get(moeda_destino)

    if taxa is None:
        print("Não temos essa moeda!")
        continue

    valor_convertido = valor / taxa

    print(f"O valor final convertido ficou em R${valor_convertido:,.2f}")
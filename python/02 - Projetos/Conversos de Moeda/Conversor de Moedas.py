taxas = {
    "usd": 5.5,
    "dolar": 5.5,
    "euro": 5.7,
    "pesos": 0.3
}

while True:

    valor = input('Qual o valor? (Ou digite "sair" para encerrar): R$')

    if valor.lower() == "sair":  # aceita sair em maiúsculas também
        print("Então é isso... Acabamos :'(....")
        break  # para o loop, finaliza o programa

    # Tratamento para garantir que o valor é número
    try:
        valor = float(valor)
    except ValueError:
        print("Por favor, digite um número válido.")
        continue  # volta para o começo do loop pedindo valor de novo

    moeda_destino = input("Para qual moeda você quer fazer a conversão?: ").strip().lower()

    taxa = taxas.get(moeda_destino)  # pega o valor da taxa direto do dicionário

    if taxa is None:
        print("q moeda e essa padrin? kk pqp")
        continue  # volta para o começo do loop, pedindo moeda de novo

    valor_convertido = valor / taxa
    print(f"Ta na mão po, o valor convertido ficou na casa dos R${valor_convertido:,.2f}.")
    if valor_convertido > valor:
        print(f"tu ganhou grana ainda safado")
    else:
        print("A coisa ta feia kk")

# criar uma lista de usuarios conhecidos

usuarios_conhecidos = ["Raul", "Likera", "Tinho", "Bixby", "Ferd", "Chapinha"]
# print(len(usuarios_conhecidos)) # qtd de nomes na lista

# Para saber se algo está dentro da lista, vamos usar o "IN"
# .append adiciona algo na lista // .remove tira algo

while True:
    print("Olá, eu sou o assistente de campo do rau7s")
    name = input("Qual o seu nome?: ").strip().capitalize()# strip() tira os espaços a mais e o capitalize() é para deixar somente a primeira letra em maiusculo

    if name in usuarios_conhecidos:
        print(f"Olá {name}, tudo bem? Tu já é de casa né cachorro")
        removed = input("Tu gostaria de ser removido da lista dog?? (y/n): ").lower()

        if removed == "y":
            usuarios_conhecidos.remove(name)
            print(f"Beleza cachorro, esperava mais de tu.... vacilao, adeus! {usuarios_conhecidos}")

    else:
        print(f"Desculpe {name}, mas ce jogou aonde??")
        adicionar_lista = input("Pensando melhor, tudo quer entrar na lista? (y/n): ").lower().strip()
        if adicionar_lista == "y":
            usuarios_conhecidos.append(name) # append que adiciona algo na lsita
            print(f"Boaa {name}, tu ta na lista irmão!!!: {usuarios_conhecidos}")
        elif adicionar_lista == "n":
            print("Tudo bem.... :'( ")









# Aqui vamos criar uma agenda simples no terminal

print("Bem vindo.")

contatos =[]

def adicionar_contato():
    nome = input("Qual o Nome do Contato?: ").title()
    numero = int(input("Qual o Número?: "))
    contatos.append(nome)
    contatos.append(numero)



while True:

    opcao_entrada_menu = int(input("Para onde você quer ir? \n1. Adicionar Contato. \n2. Lista de Contato \n3. Menu. \nDigite um número: "))

    if opcao_entrada_menu == 1:
        adicionar_contato()
    elif opcao_entrada_menu == 2:
        print(contatos)
    else:
        continue



    quest = input("Quer continuar? (s/n): ")
    if quest == "n":
        exit()
# Aqui vamos criar uma agenda simples no terminal
"""
Para salvar algo em Python, usamos a função open() com modos diferentes:

"w" → escreve do zero (apaga o que tinha antes).
"a" → adiciona (append) no final.
"r" → só leitura.
"""


import json

print("Bem vindo.")

contatos = []

# Carregar contatos salvos se existir
def carregar_contatos():
    global contatos
    """global contatos: diz que vamos alterar a variável contatos de fora da função.
        sem global, se você fizesse contatos = xxx criaria outra variável contatos."""
    try: # só p tentar e nao bugar
        """
        open abre o arquivo contatos.json no modo "r" (read).
        "with" garante que o arquivo será fechado no fim do bloco.
        "as file" dá o nome file ao objeto do arquivo. """
        with open("contatos.json", "r") as file:
            contatos = json.load(file) # lê o texto JSON do arquivo e converte para objetos Python (lista/dicionários).
    except FileNotFoundError: # se o arquivo não existe na primeira vez que rodar, caímos aqui.
            contatos = []  # Se não existir o arquivo, começa vazio

def salvar_contatos():
    global contatos
    """Salva os contatos atuais no arquivo."""
    with open("contatos.json", "w") as file: # abre o arquivo no modo "w" (write/escrita).
        json.dump(contatos, file, indent=4) # transforma a lista/dicionários em JSON e escreve no arquivo.
        # indent=4 formata com recuo de 4 espaços (p ler melhor).



def adicionar_contato():
    nome = input("Qual o Nome do Contato?: ").title()
    numero =input("Qual o Número?: ") # tirei o int
    contato = {"Nome: ": nome, "Número: ": numero}
    contatos.append(contato)
    salvar_contatos()



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
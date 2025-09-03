# Aqui vamos criar uma agenda simples no terminal
"""
Para salvar algo em Python, usamos a função open() com modos diferentes:

"w" → escreve do zero (apaga o que tinha antes).
"a" → adiciona (append) no final.
"r" → só leitura.
"""


import json

print("Bem vindo.")

def menu():
    print("\n=== MENU ===")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Sair")
    try:
        return int(input("Digite sua opção: ")) # lê a opção do usuário e tenta converter para inteiro.
    except ValueError:
        return 0 # se o usuário digitar algo que não é número, a função retorna 0 (opção inválida). → p programa n quebrar.


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
    if not nome.strip():
        print("Não podemos aceitar esse nome.")
        return contatos
    
    numero =input("Qual o Número?: ") # tirei o int
    if not numero.isdigit():
        print("Não podemos aceitar isso.")
        return contatos

    contato = {"Nome": nome, "Número": numero}
    contatos.append(contato)
    salvar_contatos() #já salva no arquivo após a inclusão (assim não perde dados se encerrar o programa).

def listar_contatos():
    if not contatos:
        print("Não há nenhum contato.")
    else:
        for x,contato in enumerate(contatos, start=1): # percorre a lista, devolvendo (índice, elemento). start=1 faz a contagem começar em 1.
            print(f"{x}. Nome: {contato['Nome']}, Número: {contato['Número']}") # acessa os dados do dicionário.

carregar_contatos()

while True:
    opcao = menu()
    if opcao == 1:
        adicionar_contato()
    elif opcao == 2:
        listar_contatos()
    elif opcao == 3:
        print("Saindo, até mais.")
        exit()
    else:
        print("Inválido")
    
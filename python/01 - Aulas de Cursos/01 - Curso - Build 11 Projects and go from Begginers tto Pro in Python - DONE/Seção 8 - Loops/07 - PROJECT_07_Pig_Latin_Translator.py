# O segredo para conseguir fazer um código é dividir o problema em pequenas partes.
#  Vamos seguir um roteiro:


# Passo 1: Receber a frase do usuário
frase_original = input("Olá, por favor me diga uma frase: ").strip().lower()

# Passo 2: Separar a frase em palavras
palavras = frase_original.split()

# Passo 3: Criar uma lista para as palavras que vao ser traduzidas
novas_palavras = []

# Passo 4: Traduzir cada palavra
for palavra in palavras:
    # 1: Pegar a primeira letra
    primeira_letra = palavras[0]

    # 2: Verificar se a primeira letra é vogal
    if primeira_letra in "aeiou":
        # Se for vogal, vamos adicionar "yay" no final
        palavra_traduzida = palavra + "yay"

    else:
        # Se for consoante, a gente precisa saber onde as vogais começam
        # E quantas consoantes tem no início

        # Criar variavel p contar consoantes
        consoantes_iniciais = 0

        # Percorrer por cada letra da palavar
        for letra in palavra:
            # Se a palavra nao for vogal
            if letra not in "aeiou":
                # Aumentamos nosso numero de consoante
                consoantes_iniciais = consoantes_iniciais + 1
            else:
                # Se encontrar a primeira vogal, paramos de contar
                break
        # Agora que sabemos quantas consoantes tem no começo, vamos traduzir
        # Pega as consoantes do inicio (até onde nosso contador chegou)
        consoantes = palavra[:consoantes_iniciais]

        # Pega o resto da palavra (a partir da primeira vogal)
        resto_da_palavra = palavra[consoantes_iniciais:]

        # Juntar tudo na ordem correta
        palavra_traduzida = resto_da_palavra + consoantes + "yay"

        # Depois de traduzir, colocar ela na lista
        novas_palavras.append(palavra_traduzida)

# P juntar tudo, usar o .join()
frase_traduzida = ' '.join(novas_palavras)

print(frase_traduzida)
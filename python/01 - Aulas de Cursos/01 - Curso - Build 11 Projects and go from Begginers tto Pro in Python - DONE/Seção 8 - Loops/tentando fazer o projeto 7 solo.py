# recebdno o usuário
frase_original = input("diga uma frase: ").strip().lower()

# separando por palavra
palavras = frase_original.split()

# criando uma lista ps palavras traduzidas -- vazia
palavras_traduzidas_final = []

# vendo se é vogal
for palavra in palavras: # for cada palavinha dentro da lista de palavras

    primeira_letra = palavra[0] # usando index p pegar a primeira letra

    if primeira_letra in "aeiou": # se a primeira letra for vogal 
        palavra_traduzida = palavra + "yay"
    
    else: # se nao for vogal

        contador_consoante = 0

        for letra in palavra:
            if letra not in "aeiou":
                contador_consoante = contador_consoante + 1
            else:
                break
        
        consoante = palavra[:contador_consoante]

        resto_palavra = palavra[contador_consoante:]

        nova_palavra = resto_palavra + consoante + "ay"
    
        palavra_traduzida = nova_palavra

    palavras_traduzidas_final.append(palavra_traduzida)

juntando_tudo = ' '.join(palavras_traduzidas_final)
print(juntando_tudo)
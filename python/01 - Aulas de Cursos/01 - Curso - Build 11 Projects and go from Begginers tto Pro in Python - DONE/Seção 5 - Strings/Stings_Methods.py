# string.method()

print("text".count("o")) # Contando quantas vezes a letra aparece

# Usar com variaveis funciona tmb
text = "bom dia mundo e Vai Palmeiras!!"
print(f'A letra "A" no texto "{text}" aparece {text.count("a")} vezes!')

#.lower e .upper para deixar tudo minusculo ou maiusculo
print(text.lower())
print(text.upper())
# OBS. Isso não vai mudar a variavel para sempre, só vai modificar ela quando vc chamar
# P modificar, tem q colocar == text = text.upper()

# Para primeira palavra vir com letra maiuscula é o .capitalize()
print(text.capitalize())

# Para todas as palavras virem com a primeira em maiusculo é o .title()
print(text.title())

# Para saber se nossa vairavel, é alguma coisa, só usar o .isxxx(), ex:
print(text.islower())
print(text.isupper())
print(text.istitle())
print(text.isalnum()) # letra e numero
print(text.isdigit())

# Cada letra tem seu espaço, e a primeia letra é a 0!
print(text.index("Palmeiras"))
print(text[0]) # Aqui vamos pegar só o ponto 0


# Para remover algo do nosso texto, usar o .strip()
# .lstrip() - remove da esquerda // r.strip() remove da direita, // .strip remove de td
print(text.strip("!"))

# .strip() sem nada, tmb serve p limpar os espaços vazios -- bem legal
# teste = input("Qual seu nome? ") # Colocar espaços após escrever o nome para dar certo
# print(len(teste))

# real = input("Qual seu nome? ").strip()
# print(len(real))

# para pegar uma parte especifica do texto: variavel[start:end:slice]
print(text[0:4:1])
# End tem que colocar um numero a mais, para pegar a letra que vc quer de fato -- slice é quantas palavras vai pular
# Se eu queiser até o final, posso fazer só text[3:] // se quiser pular text[3::2]
# Se eu quiser até a 5 text[:5]
# Para inverter todo o código text[::-1] kk que zorra
print(text[::-1])

bigtext = "UmTextoEnormeEOPalmeirasTemQueGanharAmanhã"

# para achar onde está algo, usamos o string.index("xxx")
print(bigtext.index("Texto"))

# Para pegar somente de uma parte até a outras, dentro do mesmo texto;
print(bigtext[bigtext.index("Texto"):bigtext.index("Que")])
print(bigtext[bigtext.index("Enorme"):bigtext.index("EOP")])
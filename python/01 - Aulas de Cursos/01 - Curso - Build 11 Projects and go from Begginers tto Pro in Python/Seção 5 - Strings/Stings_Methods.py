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
teste = input("Qual seu nome? ") # Colocar espaços após escrever o nome para dar certo
print(len(teste))

real = input("Qual seu nome? ").strip()
print(len(real))


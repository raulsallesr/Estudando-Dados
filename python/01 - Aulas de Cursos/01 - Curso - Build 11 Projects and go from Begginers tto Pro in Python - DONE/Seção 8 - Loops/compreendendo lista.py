
# for x -- esse x pega o valor de cada numero
# if x % 2 == 0 -- quer dizer numeros pares
numeros_pares = [x for x in range(1,101) if x % 2 == 0]
print(numeros_pares)

numeros_impares = [x for x in range(1,101) if x % 2 != 0]
print(numeros_impares)

# top:
palavras = ["Palmeiras", "vila mariana", "sorvete"]
resposta = [[x.upper(), x.lower(), len(x)] for x in palavras] # x vai virar cada palavra
print(resposta)

seila = ["oiii", "tchau", "byebye"]
resp = [[x.upper(), x.lower(), x.title(), len(x)] for x in seila]
print(resp)
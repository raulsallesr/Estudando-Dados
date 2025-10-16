# é melhor q o excel quando o arquivo é grande, usamos o pandas com usa facilidade maior
# temos as series e o DataFrame

#Séries sao 1d
# pd.Series(data, index=index)

# Dataframe é uma tabela excel
# precisamos criar um dicionario praticamente

#Dados:
lista_a = [12,5,3,1,69]
lista_b = ['a','b','c','d','e']

import pandas as pd

serie_1 = pd.Series(lista_a)
print(serie_1) # A série é indexada, a coluna a esquerda deixa numerica
# print(serie_1.size)
# print(serie_1.cumsum) # Soma acumulada
# print(serie_1.mean) # Média

# Usar indice de outra lista
serie_2 = pd.Series(lista_a, index=lista_b)
print(serie_2)
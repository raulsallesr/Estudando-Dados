# Módulos sao extensões do py
# import Nome_Modulo

"""import math as m
a = m.cos(0)
print(a)
y = m.sin(a)
print(y)
p = m.pi
print(p)"""

file_path = 'cea_01- vamos ver.txt'
with open(file_path) as f: # with open abrimos e fechamos o arq
    f_data = f.readlines()
    f.closed

lista_colunas = f_data[1].split(',')# 0 primeira linha
print(lista_colunas)

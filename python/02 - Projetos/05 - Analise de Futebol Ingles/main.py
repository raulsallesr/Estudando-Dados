# Objetivo: pegar o .txt e passar p um csv

import re
import pandas as pd

input_path = '02 - Projetos/05 - Analise de Futebol Ingles/1-premierleague.txt'
output_path = '02 - Projetos/05 - Analise de Futebol Ingles/teste01.csv'

with open(input_path, "r", encoding="utf-8") as f:
    linhas = f.readlines()

# 1º ver as primeiras linhas p ver o formato
print("-- COMEÇO Primeiras 20 linhas do arquivo (preview) --")
for l in linhas[:20]:
    print(l.strip())
print("-- FIM 20 linhas do arquivo (preview) --")
    
# 2º pegar o padrão com re COM HORA
pattern_time = re.compile(
    r'^\s*' # ^ = início da linha. I \s* = zero ou mais espaços.
    r'(\d{1,2}\.\d{2})' # \d{1,2} → 1 ou 2 dígitos (hora). I \. → ponto literal. I  \d{2} → 2 dígitos (minutos).
    r'\s+'  # \s+ → um ou mais espaços.                    
    r'(.+?)' # .+? → qualquer coisa, mas não tudo (para não engolir demais).   Captura o time da casa → grupo 2.               
    r'\s+v\s+' # \s+v\s+ → o “v” que separa os times (com espaços dos dois lados).    
    r'(.+?)'    # (.+?) → time visitante → grupo 3.                   
    r'\s+(\d{1,2}-\d{1,2})' # \s+(\d{1,2}-\d{1,2})       
    r'(?:\s+\(([^)]*)\))?'
    """
    (?: ... ) → grupo não capturante.
    \s+\( → espaço + abre parêntese.
    ([^)]*) → tudo até fechar parêntese → grupo 5 (placar do intervalo).
    \) → fecha parêntese.
    ? → esse bloco inteiro é opcional.
    """  
    , re.IGNORECASE) # re.IGNORECASE → case-insensitive.

# mesma coisa só q sem hora
pattern_no_time = re.compile(
    r'^\s*'
    r'(.+?)'
    r'\s+v\s+'
    r'(.+?)'
    r'\s+(\d{1,2}-\d{1,2})'
    r'(?:\s+\(([^)]*)\))?'
    , re.IGNORECASE)

# ^\s* → começo da linha + espaços opcionais.
# (Mon|Tue|...) → se a linha começa com dia da semana.
date_line_re = re.compile(r'^\s*(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b', re.IGNORECASE)

partidas = []
current_date = None
current_matchday = None
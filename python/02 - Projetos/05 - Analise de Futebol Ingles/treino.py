linha = "20.00  Manchester United FC    v Fulham FC                1-0 (0-0)"

# Separar a hora
hora = linha[:5]
print(hora)

# Separa nome time e placar
resto = linha[5:]
print(resto)

#separa os times pelo V

times = resto.split('v')
print(times)

time_casa = times[0].strip()          # "Manchester United FC"
print(time_casa)

time_visitante = times[1].split()[0]  # "Fulham FC" (ainda temos que tratar o placar depois)
print(time_visitante)

placar = times[1].split()[-2]         # "1-0"
print(placar)

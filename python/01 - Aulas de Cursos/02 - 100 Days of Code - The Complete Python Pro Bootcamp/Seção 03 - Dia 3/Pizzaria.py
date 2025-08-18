# P 15
#M 20
#G 25
#Bordas:
#Cheddar + 3
#Queijo + 2
#Chocolate + 5

print("Bem vindo a Pizzaria Palestra!")
valor = 0
tamanho = input("Qual tamanho da pizza verdão? P, M ou G?").lower().strip()
borda = input("Vai querer borda recheada verdão? (s/n)").lower().strip()

if tamanho == "p":
    valor += 15
elif tamanho == "m":
    valor += 20
elif tamanho == "g":
    valor += 25
else:
    print("Não temos esse tamanho")

if borda == "s":
    opcao_borda = int(input("Qual borda vai ser? 1 - Cheddar; 2 - Queijo; 3 - Chocolate"))
        
    if opcao_borda == 1:
        valor += 3
        print(f"Tua pizza ficou no valor de {valor}")
    elif opcao_borda == 2:
        valor +=2
        print(f"Tua pizza ficou no valor de {valor}")
    elif opcao_borda == 3:
        valor +=5
        print(f"Que escolhaaaa padrin!!! Tua pizza ficou no valor de {valor}")
else:
    print(f"Tua pizza ficou no valor de {valor}")
    
    
    
    

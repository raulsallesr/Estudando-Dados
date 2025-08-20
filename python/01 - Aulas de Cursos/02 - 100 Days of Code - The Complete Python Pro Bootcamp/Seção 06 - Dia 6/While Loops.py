def direita():
    turn_left()
    turn_left()
    turn_left()
    
def jogada():
    move()
    turn_left()
    move()
    direita()
    move()
    direita()
    move()
    turn_left()
   
while at_goal() is not True:
    jogada()

    # For loops é para iterar sobre uma lista
    
    # While Loops é para continuar rodando até virar falso
    # ou se nunca for falso, vai ficar p sempre :)

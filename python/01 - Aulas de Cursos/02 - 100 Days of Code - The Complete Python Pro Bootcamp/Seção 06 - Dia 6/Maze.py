def direita():
    turn_left()
    turn_left()
    turn_left()

def jogada_de_mestre():
    if right_is_clear():
        direita()
        move()
    if wall_in_front():
        turn_left()
    if wall_on_right() and front_is_clear():
        move()

    
while not at_goal():
    if wall_in_front():
        jogada_de_mestre()
    else:
        move()

# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.

def direita():
    turn_left()
    turn_left()
    turn_left()

def jogada():
    turn_left()
    while wall_on_right():
        move()
    direita()
    move()
    direita()
    while front_is_clear():
        move()
    turn_left()       
        
while not at_goal():
    if wall_in_front():
        jogada()
    else:
        move()

# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.

def direita():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
        if front_is_clear():
            move()
    elif right_is_clear():
        direita()
        move()

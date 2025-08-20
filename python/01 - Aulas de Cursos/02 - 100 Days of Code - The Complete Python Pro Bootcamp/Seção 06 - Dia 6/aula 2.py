# aula 2 do robozinho, bala demais

def direita():
    turn_left()
    turn_left()
    turn_left()
    
def movimento():
    move()
    turn_left()
    move()
    direita()
    move()
    direita()
    move()
    turn_left()

for x in range(6):
    movimento()
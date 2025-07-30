# AND, OR e NOT

print(not True)

print(not 4 == 3)

num1 = 13
num2 = 27

if not num1 > num2:
    print("NOT - Deu certo")

# O NOT dá o oposto da frase
# NOT True = False
# NOT False = True

# AND é o "E", bem basico
if num2 > num1 and num2 > 10:
    print("AND - Certo")

if not (num2 > num1 and num2 == 10):
    print("NOT / AND - Dá certo, pq num2 não é 10, e colocamos o NOT antes :)")

# OR aceita se um deles for vdd
if num2 > num1 or num2 == 10:
    print("OR -  Dá certo, pq num2 é maior que num1")

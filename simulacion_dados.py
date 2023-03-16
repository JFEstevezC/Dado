import random


dado1 = random.randint(1,6)

if (dado1 == 1):
    rta = "Cara opuesta: 6"
elif (dado1 == 2):
    rta = "Cara opuesta: 5"
elif (dado1 == 3):
    rta = "Cara opuesta: 4"
elif (dado1 == 4):
    rta = "Cara opuesta: 3"
elif (dado1 == 5):
    rta = "Cara opuesta: 2"
else:
    rta = "Cara opuesta: 1"
print("Cara dado 1: " +str(dado1) + " --> " + rta )

dado2 = random.randint(1,6)

if (dado2 == 1):
    rta = "Cara opuesta: 6"
elif (dado2 == 2):
    rta = "Cara opuesta: 5"
elif (dado2 == 3):
    rta = "Cara opuesta: 4"
elif (dado2 == 4):
    rta = "Cara opuesta: 3"
elif (dado2 == 5):
    rta = "Cara opuesta: 2"
else:
    rta = "Cara opuesta: 1"
print("Cara dado 2: " +str(dado2) + " --> " + rta )

if dado1 == dado2:
    rta = "Al lanzar los dados salió par"
else:
    rta = "Al lanzar los dados no salió par"
print(rta)
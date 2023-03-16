dado = int(input("Digite la cara del dado: "))

if (dado == 1):
    rta = "Cara opuesta: 6"
elif (dado == 2):
    rta = "Cara opuesta: 5"
elif (dado == 3):
    rta = "Cara opuesta: 4"
elif (dado == 4):
    rta = "Cara opuesta: 3"
elif (dado == 5):
    rta = "Cara opuesta: 2"
else:
    rta = "Cara opuesta: 1"
print(rta)

# Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44, etc. 
#(No se ingresan valores por teclado)

def while_exercise4():
    i = 0
    j = 11
    while (i < 25):
        print(f'{j}', end =' - ')
        j += 11
        i += 1

while_exercise4()
    
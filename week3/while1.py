#Escribir un programa que solicite ingresar 10 notas de alumnos
#y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

def while_exercise1():
    notes = []
    i = 0
    while (i  < 10):
        notes.append(int(input('inserte nota de estudiantes:')))
        i += 1
    
    less = more = 0

    j = 0
    while ( j < 10):
        if (notes[j] < 7):
            less += 1
        else:
            more += 1
        j += 1
    print(f'{less}estudiantes tienen notas menores a 7')
    print(f'{more} estudiantes tienen notas mayores o iguales a 7')

    return 1

while_exercise1()
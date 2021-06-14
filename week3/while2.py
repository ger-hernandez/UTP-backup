#Se ingresan un conjunto de n alturas de personas por teclado.
#Mostrar la altura promedio de las personas.
import math
def while_exercise2(s):
    i = 0
    l = len(s)
    su = 0
    while (i < l):
        su += s[i]
        i += 1

    return f'el promedio es: {(su // l)}'

l = [3, 6, 9]

print(while_exercise2(l))

    
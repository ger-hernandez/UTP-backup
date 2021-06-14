#Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16 - 24, etc.
def while_exercise5():
    i = 1
    m = 8
    r = 0
    while r < 500:
        r =  m * i
        print(f'{r}', end = '-')
        i += 1

while_exercise5()